from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver

from generator.failure_emitter import FailureEmitter, FailureLabel


def _load_schema(schema_path: Path) -> dict:
    return json.loads(schema_path.read_text(encoding="utf-8"))


def _get_validator(schema_dir: Path, schema_name: str) -> Draft202012Validator:
    schema = _load_schema(schema_dir / schema_name)
    base_uri = schema_dir.as_uri().rstrip("/") + "/"
    resolver = RefResolver(base_uri=base_uri, referrer=schema)
    return Draft202012Validator(schema, resolver=resolver)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate overlay descriptor.")
    parser.add_argument("overlay_path", type=Path, help="Overlay descriptor JSON path.")
    parser.add_argument(
        "--schema-dir",
        type=Path,
        default=Path("schemas"),
        help="Schema directory.",
    )
    parser.add_argument(
        "--run-id",
        type=str,
        default="local-run",
        help="Run identifier for failure logs.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    overlay = json.loads(args.overlay_path.read_text(encoding="utf-8"))
    validator = _get_validator(args.schema_dir, "overlay-descriptor.json")
    errors = sorted(validator.iter_errors(overlay), key=lambda e: e.path)
    if not errors:
        operations = overlay.get("operations", [])
        paths = [op.get("path") for op in operations]
        if len(paths) != len(set(paths)):
            errors.append(
                Exception("Overlay contains duplicate operation paths, ambiguous interpretation.")
            )
        scope = overlay.get("precedence", {}).get("scope", "")
        notes = overlay.get("precedence", {}).get("notes", "")
        if scope == "global" and "explicit" not in notes.lower():
            errors.append(Exception("Global overlay scope requires explicit precedence notes."))
    if errors:
        evidence = {
            "errors": [
                {
                    "message": getattr(error, "message", str(error)),
                    "path": list(getattr(error, "path", [])),
                    "schema_path": list(getattr(error, "schema_path", [])),
                }
                for error in errors
            ]
        }
        failure = FailureLabel(
            Type="schema_failure",
            message="Overlay descriptor validation failed",
            phase_id="validate",
            evidence=evidence,
        )
        FailureEmitter(Path("artifacts/failures")).emit(failure, run_id=args.run_id)
        print(f"Overlay validation failed: {failure.as_dict()}")
        return 1
    print(f"Overlay validation passed: {args.overlay_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
