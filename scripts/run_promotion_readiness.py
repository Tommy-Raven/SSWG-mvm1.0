from __future__ import annotations

import argparse
import json
from pathlib import Path

from generator.determinism import (
    bijectivity_check,
    replay_determinism_check,
    write_bijectivity_report,
    write_determinism_report,
)
from generator.failure_emitter import FailureEmitter, FailureLabel, validate_failure_label
from generator.pdl_validator import PDLValidationError, validate_pdl_file_with_report
from generator.phase_io import build_phase_io_manifest, detect_phase_collapse, load_pdl, write_manifest
from generator.anchor_registry import AnchorRegistry, enforce_anchor
from generator.hashing import hash_data


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run promotion readiness gates.")
    parser.add_argument(
        "--run-id",
        type=str,
        default="local-run",
        help="Run identifier.",
    )
    parser.add_argument(
        "--pdl-path",
        type=Path,
        default=Path("pdl/example_full_9_phase.yaml"),
        help="PDL path to validate.",
    )
    parser.add_argument(
        "--schema-dir",
        type=Path,
        default=Path("schemas"),
        help="Schema directory.",
    )
    parser.add_argument(
        "--phase-outputs",
        type=Path,
        default=Path("tests/fixtures/phase_outputs.json"),
        help="Phase outputs fixture for determinism replay.",
    )
    parser.add_argument(
        "--measurement-ids",
        type=Path,
        default=Path("tests/fixtures/measurement_ids.json"),
        help="Measurement identifiers fixture.",
    )
    parser.add_argument(
        "--observed-io",
        type=Path,
        default=Path("tests/fixtures/observed_io.json"),
        help="Observed IO fixture for phase IO manifest.",
    )
    parser.add_argument(
        "--evidence-dir",
        type=Path,
        default=Path("artifacts/evidence_pack"),
        help="Evidence pack output directory.",
    )
    parser.add_argument(
        "--anchor-registry",
        type=Path,
        default=Path("config/anchor_registry.json"),
        help="Anchor registry path.",
    )
    parser.add_argument(
        "--overlays-dir",
        type=Path,
        default=Path("overlays"),
        help="Overlay descriptor directory.",
    )
    return parser.parse_args()


def _gate_failure(emitter: FailureEmitter, run_id: str, failure: FailureLabel) -> int:
    emitter.emit(failure, run_id=run_id)
    print(f"Promotion readiness gate failed: {failure.as_dict()}")
    return 1


def main() -> int:
    args = _parse_args()
    evidence_dir = args.evidence_dir / args.run_id
    evidence_dir.mkdir(parents=True, exist_ok=True)
    failure_emitter = FailureEmitter(evidence_dir / "failures")

    try:
        validate_pdl_file_with_report(
            pdl_path=args.pdl_path,
            schema_dir=args.schema_dir,
            report_dir=evidence_dir / "validation",
            run_id=args.run_id,
        )
    except PDLValidationError as exc:
        failure = FailureLabel(
            Type=exc.label.Type,
            message=exc.label.message,
            phase_id="validate",
            evidence=exc.label.evidence,
        )
        return _gate_failure(failure_emitter, args.run_id, failure)

    validation_reports = list((evidence_dir / "validation").glob("pdl_validation_*.json"))
    if validation_reports:
        report_path = validation_reports[0]
        report_payload = json.loads(report_path.read_text(encoding="utf-8"))
        anchor_failure = enforce_anchor(
            artifact_path=report_path,
            metadata=report_payload.get("anchor", {}),
            registry=AnchorRegistry(args.anchor_registry),
        )
        if anchor_failure:
            return _gate_failure(failure_emitter, args.run_id, anchor_failure)

    pdl_obj = load_pdl(args.pdl_path)
    observed = json.loads(args.observed_io.read_text(encoding="utf-8"))
    manifest = build_phase_io_manifest(pdl_obj, observed)
    collapse = detect_phase_collapse(manifest, pdl_obj)
    if collapse:
        return _gate_failure(failure_emitter, args.run_id, collapse)
    write_manifest(evidence_dir / "phase_io_manifest.json", manifest)

    phase_outputs = json.loads(args.phase_outputs.read_text(encoding="utf-8"))
    failure, report = replay_determinism_check(
        run_id=args.run_id,
        phase_outputs=phase_outputs,
        required_phases=["normalize", "analyze", "validate", "compare"],
    )
    write_determinism_report(evidence_dir / "determinism_report.json", report)
    if failure:
        return _gate_failure(failure_emitter, args.run_id, failure)
    measurement_ids = json.loads(args.measurement_ids.read_text(encoding="utf-8"))
    id_failure = bijectivity_check(measurement_ids.get("ids", []))
    write_bijectivity_report(
        evidence_dir / "bijectivity_report.json",
        measurement_ids.get("ids", []),
        id_failure,
    )
    if id_failure:
        return _gate_failure(failure_emitter, args.run_id, id_failure)

    registry = AnchorRegistry(args.anchor_registry)
    registry_data = registry.load()
    overlays = []
    if args.overlays_dir.exists():
        overlays = [
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(args.overlays_dir.glob("*.json"))
        ]
    overlay_payload = {
        "anchor": {
            "anchor_id": "overlay_chain_manifest",
            "anchor_version": "1.0.0",
            "scope": "run",
            "owner": "scripts.run_promotion_readiness",
            "status": "draft",
        },
        "run_id": args.run_id,
        "registry_snapshot": registry_data,
        "overlays": overlays,
    }
    overlay_payload["inputs_hash"] = hash_data(overlay_payload)
    (evidence_dir / "overlay_chain_manifest.json").write_text(
        json.dumps(overlay_payload, indent=2),
        encoding="utf-8",
    )

    try:
        validate_failure_label(
            FailureLabel(
                Type="schema_failure",
                message="Failure label validation check",
                phase_id="validate",
            )
        )
    except ValueError as exc:
        return _gate_failure(
            failure_emitter,
            args.run_id,
            FailureLabel(
                Type="tool_mismatch",
                message=str(exc),
                phase_id="validate",
            ),
        )

    print(f"Promotion readiness gates passed. Evidence at {evidence_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
