"""
Test the SSWG–MVM main pipeline.
"""

from generator.main import run_mvm
import os
import json


def test_run_mvm_end_to_end(tmp_path):
    out_dir = tmp_path / "outputs"
    wf_path = tmp_path / "wf.json"

    wf_path.write_text(json.dumps({
        "workflow_id": "test",
        "version": "v.09.mvm.25",
        "metadata": {"purpose": "Test"},
        "phases": [],
    }))

    refined = run_mvm(wf_path, out_dir=out_dir, preview=False)
    assert isinstance(refined, dict)
    assert "workflow_id" in refined
