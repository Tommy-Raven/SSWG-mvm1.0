#!/usr/bin/env python3
"""
generator/main.py

AI Instructional Workflow Generator
Produces a minified JSON workflow document according to the "Grimoire" schema.
Usable as both a CLI tool and an importable module.

Example CLI:
    python -m generator.main --purpose "Teach AI to build chatbots" \
        --audience "beginners" --style "technical" \
        --out ./build/ai_workflow_output.json --pretty

Example programmatic use:
    from generator.main import generate_workflow, export_minified_json
    wf = generate_workflow({"purpose": "X", "audience": "Y", "style": "Z"})
    export_minified_json(wf, "./out.json", pretty=False)
"""

from __future__ import annotations
import json
import uuid
import datetime
import os
import argparse
import logging
from typing import Dict, Any, Optional

# Configure module logger
logger = logging.getLogger("generator")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)


# -------------------------------------------------------------------------
# Schema Builders
# -------------------------------------------------------------------------

def build_metadata(user_inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Construct the metadata block for the workflow."""
    now = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    metadata = {
        "author": user_inputs.get("author", "Tommy Raven"),
        "created": user_inputs.get("created", now),
        "purpose": user_inputs.get(
            "purpose", "Teach AI to create instructional workflows dynamically"
        ),
        "audience": user_inputs.get("audience", "General"),
        "style": user_inputs.get("style", "Technical"),
        "language": user_inputs.get("language", "en-US"),
        "expansion_mode": user_inputs.get("expansion_mode", ["recursive", "modular"]),
        "evaluation_metrics": user_inputs.get(
            "evaluation_metrics",
            ["clarity", "coverage", "expandability", "translatability"],
        ),
    }
    return metadata


def build_phases() -> list:
    """Build canonical five-phase description used by the generator."""
    return [
        {
            "id": "P1",
            "title": "Initialization & Variable Acquisition",
            "input": ["user_prompt"],
            "output": ["objective", "audience", "context"],
            "submodules": [
                {
                    "id": "M1A",
                    "name": "ObjectiveRefinement",
                    "inputs": ["user_prompt"],
                    "outputs": ["objective"],
                    "ai_logic": "Convert abstract goals to measurable actions.",
                },
                {
                    "id": "M1B",
                    "name": "ContextMapping",
                    "inputs": ["audience"],
                    "outputs": ["context"],
                    "ai_logic": "Identify audience profile and contextual parameters.",
                },
            ],
            "expansion_hooks": ["P2"],
            "ai_task_logic": "Prompt user for intent, parse metadata, store structured context.",
            "human_actionable": "Answer initialization prompts with detailed goal statements.",
        },
        {
            "id": "P2",
            "title": "Human-Readable How-To Generation",
            "input": ["objective", "audience"],
            "output": ["structured_instruction"],
            "submodules": [
                {
                    "id": "M2A",
                    "name": "StageWriter",
                    "ai_logic": "Draft stage-by-stage how-to guide based on objective and audience.",
                },
                {
                    "id": "M2B",
                    "name": "StepDetailer",
                    "ai_logic": "Expand each stage into steps, actions, and expected outcomes.",
                },
            ],
            "expansion_hooks": ["P3"],
            "ai_task_logic": "Generate readable instructional stages with step-by-step clarity.",
            "human_actionable": "Follow generated instructions to achieve the stated objective.",
        },
        {
            "id": "P3",
            "title": "Modular Expansion & Reusability",
            "input": ["structured_instruction"],
            "output": ["modular_workflow"],
            "submodules": [
                {
                    "id": "M3A",
                    "name": "ModuleGraphBuilder",
                    "ai_logic": "Generate dependency graph for workflow modules.",
                },
                {
                    "id": "M3B",
                    "name": "DependencyResolver",
                    "ai_logic": "Detect and resolve circular or missing dependencies.",
                },
            ],
            "ai_task_logic": "Split workflow into reusable atomic modules with dependency tags.",
            "human_actionable": "Reuse or recombine generated modules for new objectives.",
        },
        {
            "id": "P4",
            "title": "Evaluation & Quality Assurance",
            "input": ["modular_workflow"],
            "output": ["evaluation_report"],
            "submodules": [
                {
                    "id": "M4A",
                    "name": "ClarityAssessor",
                    "ai_logic": "Rate instructional clarity for human readability.",
                },
                {
                    "id": "M4B",
                    "name": "CoverageTester",
                    "ai_logic": "Check completeness and logical coverage of workflow.",
                },
                {
                    "id": "M4C",
                    "name": "TranslatorValidator",
                    "ai_logic": "Test if workflow is interpretable by another AI.",
                },
            ],
            "ai_task_logic": "Run diagnostics on clarity, coverage, and AI-translatability.",
            "human_actionable": "Review evaluation summary; approve or request refinements.",
        },
        {
            "id": "P5",
            "title": "Regeneration & Evolution",
            "input": ["evaluation_report", "user_feedback"],
            "output": ["improved_workflow"],
            "submodules": [
                {
                    "id": "M5A",
                    "name": "VersionManager",
                    "ai_logic": "Track workflow versions and changes.",
                },
                {
                    "id": "M5B",
                    "name": "FeedbackIntegrator",
                    "ai_logic": "Merge human and AI feedback into improved template.",
                },
            ],
            "ai_task_logic": "Integrate feedback and regenerate optimized workflow iterations.",
            "human_actionable": "Provide detailed notes to guide refinement.",
        },
    ]


def build_dependency_graph() -> Dict[str, Any]:
    """Canonical dependency graph for the five-phase pipeline."""
    return {
        "nodes": ["P1", "P2", "P3", "P4", "P5"],
        "edges": [["P1", "P2"], ["P2", "P3"], ["P3", "P4"], ["P4", "P5"]],
    }


def assemble_workflow(user_inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Compose the full workflow data structure."""
    workflow_id = f"ai_instructional_workflow_{uuid.uuid4().hex[:8]}"
    return {
        "workflow_id": workflow_id,
        "version": user_inputs.get("version", "3.0"),
        "title": user_inputs.get("title", "AI Instructional Workflow Generator"),
        "metadata": build_metadata(user_inputs),
        "phases": build_phases(),
        "dependency_graph": build_dependency_graph(),
        "versioning": {
            "parent_id": user_inputs.get("parent_id"),
            "child_workflows": user_inputs.get("child_workflows", []),
            "auto_regeneration": user_inputs.get("auto_regeneration", True),
        },
    }


# -------------------------------------------------------------------------
# IO / Export Helpers
# -------------------------------------------------------------------------

def export_minified_json(
    data: Dict[str, Any],
    out_path: str,
    pretty: bool = False,
    overwrite: bool = True,
) -> str:
    """Write JSON to out_path. If pretty==False, writes minified JSON."""
    if not out_path:
        raise ValueError("out_path must be provided")

    out_dir = os.path.dirname(os.path.abspath(out_path)) or "."
    os.makedirs(out_dir, exist_ok=True)

    if os.path.exists(out_path) and not overwrite:
        raise FileExistsError(f"File exists and overwrite=False: {out_path}")

    if pretty:
        serialized = json.dumps(data, indent=2, sort_keys=False, ensure_ascii=False)
    else:
        serialized = json.dumps(data, separators=(",", ":"), ensure_ascii=False)

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(serialized)

    logger.info("Workflow saved to %s", out_path)
    return out_path


# -------------------------------------------------------------------------
# CLI
# -------------------------------------------------------------------------

def parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="generator.main", description="AI Instructional Workflow Generator"
    )
    parser.add_argument("--purpose", "-p", type=str, help="Workflow purpose/goal")
    parser.add_argument("--audience", "-a", type=str, help="Target audience")
    parser.add_argument("--style", "-s", type=str, help="Writing style or voice")
    parser.add_argument(
        "--title",
        "-t",
        type=str,
        default="AI Instructional Workflow Generator",
        help="Title of the workflow",
    )
    parser.add_argument(
        "--out",
        "-o",
        type=str,
        default="./build/ai_workflow_output.json",
        help="Output JSON path",
    )
    parser.add_argument("--pretty", action="store_true", help="Write pretty-printed JSON")
    parser.add_argument(
        "--overwrite", action="store_true", help="Allow overwriting the output file"
    )
    parser.add_argument(
        "--version", dest="version_flag", action="store_true", help="Print module version"
    )
    return parser.parse_args(argv)


def main(argv: Optional[list] = None) -> int:
    args = parse_args(argv)

    if args.version_flag:
        print("generator.main version 3.0")
        return 0

    user_inputs: Dict[str, Any] = {
        "purpose": args.purpose
        or "Teach AI to create instructional workflows dynamically",
        "audience": args.audience or "General",
        "style": args.style or "Technical",
        "title": args.title,
        "language": "en-US",
        "expansion_mode": ["recursive", "modular"],
        "evaluation_metrics": [
            "clarity",
            "coverage",
            "expandability",
            "translatability",
        ],
    }

    workflow = assemble_workflow(user_inputs)

    try:
        export_minified_json(workflow, args.out, pretty=args.pretty, overwrite=args.overwrite)
    except FileExistsError as e:
        logger.error(str(e))
        return 2
    except Exception as e:
        logger.exception("Failed to export workflow: %s", e)
        return 3

    # Show brief preview
    raw = json.dumps(workflow, separators=(",", ":")) if not args.pretty else json.dumps(workflow, indent=2)
    preview = raw[:800] + ("..." if len(raw) > 800 else "")
    print(preview)
    return 0


# -------------------------------------------------------------------------
# Public API
# -------------------------------------------------------------------------

def generate_workflow(user_inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Public function for programmatic generation."""
    return assemble_workflow(user_inputs)


if __name__ == "__main__":
    raise SystemExit(main())
