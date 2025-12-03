#!/usr/bin/env python3
"""
generator/exporters.py — Export utilities for SSWG workflows
Modernized and type-annotated, preserving custom log function.
"""

from __future__ import annotations
import os
import json
import asyncio
from typing import Coroutine
from .utils import log
from pathlib import Path
from typing import Any, Dict

from generator.utils import log  # using your existing log function


def ensure_dir_exists(path: str | Path) -> None:
    """Ensure the directory for the given path exists."""
    path = Path(path)
    os.makedirs(path.parent, exist_ok=True)


def export_markdown(workflow: Any, out_dir: str | Path = "templates") -> Path:
    """
    Export workflow to Markdown format.

    Args:
        workflow: Workflow object with structured_instruction, modular_workflow, evaluation_report.
        out_dir: Directory to save Markdown file.

    Returns:
        Path to the saved Markdown file.
    """
    out_dir = Path(out_dir)
    ensure_dir_exists(out_dir / f"{workflow.workflow_id}.md")
    filename = out_dir / f"{workflow.workflow_id}.md"

    log(f"Exporting workflow {workflow.workflow_id} → Markdown")
    md_content = f"# Workflow {workflow.workflow_id}\n\n"
    md_content += f"**Objective:** {workflow.objective}\n\n## Stages\n"

    for stage, steps in workflow.structured_instruction.items():
        md_content += f"### {stage}\n"
        for step in steps:
            md_content += f"- {step}\n"

    md_content += "\n## Modules\n"
    md_content += json.dumps(workflow.modular_workflow.get("modules", {}), indent=2)
    md_content += "\n\n## Dependencies\n"
    for dep in workflow.modular_workflow.get("dependencies", []):
        md_content += f"- {dep}\n"

    md_content += "\n\n## Evaluation Report\n"
    for k, v in (workflow.evaluation_report or {}).items():
        md_content += f"- {k.capitalize()}: {v}\n"

    filename.write_text(md_content, encoding="utf-8")
    log(f"Markdown saved at {filename}")
    return filename


def export_json(workflow: Any, out_dir: str | Path = "templates") -> Path:
    """
    Export workflow to JSON format.

    Args:
        workflow: Workflow object.
        out_dir: Directory to save JSON file.

    Returns:
        Path to the saved JSON file.
    """
    out_dir = Path(out_dir)
    ensure_dir_exists(out_dir / f"{workflow.workflow_id}.json")
    filename = out_dir / f"{workflow.workflow_id}.json"

    log(f"Exporting workflow {workflow.workflow_id} → JSON")
    data: Dict[str, Any] = {
        "workflow_id": workflow.workflow_id,
        "objective": workflow.objective,
        "stages": workflow.structured_instruction,
        "modules": workflow.modular_workflow,
        "evaluation_report": workflow.evaluation_report,
        "improved_workflow": getattr(workflow, "improved_workflow", None),
    }

    filename.write_text(json.dumps(data, indent=4), encoding="utf-8")
    log(f"JSON saved at {filename}")
    return filename


# ─── Async Helpers ────────────────────────────────────────────────


async def export_markdown_async(
    workflow: Any, out_dir: str | Path = "templates"
) -> Path:
    """Async wrapper for export_markdown."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, export_markdown, workflow, out_dir)


async def export_json_async(workflow: Any, out_dir: str | Path = "templates") -> Path:
    """Async wrapper for export_json."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, export_json, workflow, out_dir)


async def export_all_async(
    workflow: Any, out_dir: str | Path = "templates"
) -> tuple[Path, Path]:
    """
    Async helper to export both Markdown and JSON concurrently.

    Returns:
        Tuple[Path, Path]: Paths to the Markdown and JSON files.
    """
    md_task: Coroutine = export_markdown_async(workflow, out_dir)
    json_task: Coroutine = export_json_async(workflow, out_dir)
    return await asyncio.gather(md_task, json_task)
