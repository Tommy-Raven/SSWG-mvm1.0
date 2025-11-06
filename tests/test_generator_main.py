#!/usr/bin/env python3
"""
tests/test_generator_main.py

Unit tests for generator/main.py
Validates the workflow generation pipeline, ensuring internal consistency,
schema compliance, and file export functionality.

Run tests:
    pytest -v tests/test_generator_main.py
"""

import os
import json
import tempfile
import pytest

from generator.main import (
    build_metadata,
    build_phases,
    build_dependency_graph,
    assemble_workflow,
    export_minified_json,
    generate_workflow,
)

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------

@pytest.fixture
def sample_inputs():
    return {
        "author": "Tommy Raven",
        "purpose": "Test AI workflow generator",
        "audience": "Developers",
        "style": "Analytical",
        "language": "en-US",
    }

# -------------------------------------------------------------------------
# Metadata Tests
# -------------------------------------------------------------------------

def test_build_metadata_keys(sample_inputs):
    meta = build_metadata(sample_inputs)
    expected_keys = {
        "author",
        "created",
        "purpose",
        "audience",
        "style",
        "language",
        "expansion_mode",
        "evaluation_metrics",
    }
    assert expected_keys.issubset(meta.keys())
    assert meta["author"] == "Tommy Raven"


def test_build_metadata_defaults():
    meta = build_metadata({})
    assert isinstance(meta["created"], str)
    assert "Z" in meta["created"]  # UTC timestamp format
    assert meta["purpose"].startswith("Teach AI")


# -------------------------------------------------------------------------
# Phase Structure Tests
# -------------------------------------------------------------------------

def test_build_phases_structure():
    phases = build_phases()
    assert isinstance(phases, list)
    assert len(phases) == 5

    for phase in phases:
        assert "id" in phase
        assert "title" in phase
        assert "input" in phase
        assert "output" in phase
        assert "submodules" in phase
        assert "ai_task_logic" in phase
        assert "human_actionable" in phase


def test_phase_ids_unique():
    phases = build_phases()
    ids = [p["id"] for p in phases]
    assert len(ids) == len(set(ids)), "Phase IDs should be unique"


# -------------------------------------------------------------------------
# Dependency Graph Tests
# -------------------------------------------------------------------------

def test_dependency_graph_validity():
    graph = build_dependency_graph()
    assert "nodes" in graph and "edges" in graph
    for edge in graph["edges"]:
        assert all(node in graph["nodes"] for node in edge)


# -------------------------------------------------------------------------
# Workflow Assembly Tests
# -------------------------------------------------------------------------

def test_assemble_workflow_structure(sample_inputs):
    wf = assemble_workflow(sample_inputs)
    assert "workflow_id" in wf
    assert wf["version"].startswith("3.")
    assert isinstance(wf["phases"], list)
    assert "dependency_graph" in wf
    assert "metadata" in wf
    assert wf["metadata"]["audience"] == "Developers"


def test_generate_workflow_alias(sample_inputs):
    wf = generate_workflow(sample_inputs)
    assert isinstance(wf, dict)
    assert wf["metadata"]["author"] == "Tommy Raven"


# -------------------------------------------------------------------------
# Export Tests
# -------------------------------------------------------------------------

def test_export_minified_json_creates_file(sample_inputs):
    wf = assemble_workflow(sample_inputs)
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = os.path.join(tmpdir, "workflow.json")
        result_path = export_minified_json(wf, out_path, pretty=False, overwrite=True)

        assert os.path.exists(result_path)
        with open(result_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        assert "workflow_id" in data


def test_export_pretty_json_format(sample_inputs):
    wf = assemble_workflow(sample_inputs)
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = os.path.join(tmpdir, "pretty.json")
        export_minified_json(wf, out_path, pretty=True)
        text = open(out_path, "r", encoding="utf-8").read()
        assert text.startswith("{\n"), "Expected pretty JSON to start with brace+newline"


def test_export_raises_if_exists(sample_inputs):
    wf = assemble_workflow(sample_inputs)
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = os.path.join(tmpdir, "dupe.json")
        # Create first file
        export_minified_json(wf, out_path, overwrite=True)
        # Second should raise
        with pytest.raises(FileExistsError):
            export_minified_json(wf, out_path, overwrite=False)


# -------------------------------------------------------------------------
# Integration & Sanity
# -------------------------------------------------------------------------

def test_full_workflow_integration(sample_inputs):
    """Simulate full generation pipeline end-to-end."""
    wf = assemble_workflow(sample_inputs)
    assert len(wf["phases"]) == 5
    assert wf["dependency_graph"]["edges"][-1] == ["P4", "P5"]

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "ai_workflow.json")
        export_minified_json(wf, path)
        assert os.path.isfile(path)
        data = json.load(open(path))
        assert "workflow_id" in data


def test_metadata_consistency_between_calls(sample_inputs):
    meta1 = build_metadata(sample_inputs)
    meta2 = build_metadata(sample_inputs)
    assert meta1["purpose"] == meta2["purpose"]
    assert meta1["audience"] == "Developers"
