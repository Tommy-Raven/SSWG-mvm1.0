#!/usr/bin/env python3
"""
generator/main.py — Grimoire v1.0 MVM
AI Instructional Workflow Generator
-----------------------------------
Modular, phase-based workflow generator with recursive self-expansion.
Generates both human-readable (Markdown) and machine-readable (JSON) outputs.
"""

from __future__ import annotations
from pathlib import Path
import sys
import json
import argparse
import datetime
import logging
from typing import Dict, Any, Optional

# ─── Local Imports ────────────────────────────────────────────────
try:
    from ai_core.workflow import Workflow
    from ai_core.exporters import export_json, export_markdown
    from ai_recursive.expansion import generate as recursive_generate
    from ai_recursive.merging import merge as recursive_merge
    from ai_monitoring.telemetry import record as telemetry_record
    from ai_validation.schema_tracker import validate_schema
    from generator.recursion_manager import RecursionManager
    from ai_core.utils import generate_workflow_id, log
except ImportError as e:
    print(f"Error importing local modules: {e}")
    sys.exit(1)

# ─── Logging Setup ────────────────────────────────────────────────
logger = logging.getLogger("generator")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)


# ─── Input Parsing ────────────────────────────────────────────────
def parse_user_input(argv: Optional[list] = None) -> Dict[str, Any]:
    parser = argparse.ArgumentParser(description="AI Instructional Workflow Generator")
    parser.add_argument("--purpose", "-p", type=str, help="Purpose of the workflow")
    parser.add_argument("--audience", "-a", type=str, help="Target audience")
    parser.add_argument(
        "--delivery_mode", "-d", type=str, help="Delivery modes (text, code)"
    )
    parser.add_argument(
        "--expansion_mode", "-x", type=str, help="Expansion modes (recursive, modular)"
    )
    parser.add_argument("--evaluation_method", "-e", type=str, help="Evaluation method")
    parser.add_argument("--style", "-s", type=str, help="Workflow style/voice")
    parser.add_argument(
        "--title", "-t", type=str, default="AI Instructional Workflow Generator"
    )
    parser.add_argument(
        "--out", "-o", type=Path, default=Path("./data/outputs/ai_workflow_output.json")
    )
    parser.add_argument(
        "--pretty", action="store_true", help="Write pretty JSON output"
    )
    parser.add_argument(
        "--overwrite", action="store_true", help="Allow overwriting existing files"
    )
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    args = parser.parse_args(argv)

    if args.version:
        print("AI Instructional Workflow Generator v1.0 MVM")
        sys.exit(0)

    def ask(val: Optional[str], prompt: str) -> str:
        return val or input(prompt).strip()

    return {
        "purpose": ask(args.purpose, "Enter workflow purpose: "),
        "audience": ask(args.audience, "Enter target audience: "),
        "delivery_mode": [
            m.strip() for m in (args.delivery_mode or "text,code").split(",")
        ],
        "expansion_mode": [
            m.strip() for m in (args.expansion_mode or "recursive,modular").split(",")
        ],
        "evaluation_method": ask(args.evaluation_method, "Enter evaluation method: "),
        "style": ask(args.style, "Enter workflow style/voice: "),
        "title": args.title,
        "out_path": args.out,
        "pretty": args.pretty,
        "overwrite": args.overwrite,
    }


# ─── Workflow Assembly ────────────────────────────────────────────
def assemble_metadata(params: Dict[str, Any]) -> Dict[str, Any]:
    now = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return {
        "author": "Tommy Raven",
        "created": now,
        "purpose": params["purpose"],
        "audience": params["audience"],
        "style": params["style"],
        "delivery_mode": params["delivery_mode"],
        "expansion_mode": params["expansion_mode"],
        "evaluation_method": params["evaluation_method"],
        "language": "en-US",
        "schema_version": "1.0",
        "phase_metadata": {},
    }


def assemble_workflow(params: Dict[str, Any]) -> Dict[str, Any]:
    workflow_id = generate_workflow_id()
    metadata = assemble_metadata(params)

    wf = Workflow(workflow_id, params)
    wf.run_all_phases()

    # Recursive expansion (safe fallback if missing)
    try:
        expanded = recursive_merge(
            recursive_generate(
                {
                    "workflow_id": workflow_id,
                    "objective": wf.results.get("Phase 1 — Initialization", {}).get(
                        "objective", params["purpose"]
                    ),
                    "stages": wf.results.get("Phase 2 — How-To Generation", {}),
                    "modules": wf.results.get("Phase 3 — Modularization", {}),
                }
            )
        )
    except Exception as e:
        logger.warning("Recursive expansion failed: %s", e)
        expanded = {}

    # Telemetry record (optional)
    try:
        telemetry_record(workflow_id, expanded)
    except Exception:
        pass

    workflow_data = {
        "workflow_id": workflow_id,
        "title": params["title"],
        "metadata": metadata,
        "phases": wf.results,
        "recursive_expansion": expanded,
        "timestamp": metadata["created"],
    }

    try:
        validate_schema(workflow_data)
    except Exception as e:
        logger.warning("Schema validation skipped/failed: %s", e)

    return workflow_data


# ─── Export ──────────────────────────────────────────────────────
def export_all(
    workflow: Dict[str, Any],
    out_path: Path,
    pretty: bool = False,
    overwrite: bool = True,
):
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if out_path.exists() and not overwrite:
        logger.error("File exists and overwrite=False: %s", out_path)
        sys.exit(2)

    export_json(workflow, out_path, pretty)
    export_markdown(workflow)
    logger.info("Workflow export complete: JSON -> %s", out_path)


# ─── Main Entrypoint ─────────────────────────────────────────────
def main(argv: Optional[list] = None) -> int:
    params = parse_user_input(argv)
    workflow_data = assemble_workflow(params)
    export_all(workflow_data, params["out_path"], params["pretty"], params["overwrite"])

    preview = json.dumps(workflow_data, indent=2)[:800]
    print("\n--- Workflow Preview ---\n", preview, "...\n")
    logger.info("Workflow generation complete for ID: %s", workflow_data["workflow_id"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
