#!/usr/bin/env python3
"""
generator/recursion_manager.py — Recursion policy and refinement.

Provides:
- RecursionPolicy: configuration for recursion decisions.
- RecursionManager: minimal refinement metadata annotator.
- simple_refiner: MVM-friendly wrapper that makes refinement non-fatal.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional
import logging

logger = logging.getLogger("generator.recursion_manager")


@dataclass
class RecursionPolicy:
    """
    Configuration for recursion decisions.

    Attributes:
        max_depth:
            Maximum allowed recursion depth.
        min_improvement:
            Minimum score_delta required to justify another recursion step.
    """

    max_depth: int = 2
    min_improvement: float = 1.0


class RecursionManager:
    """
    Decide whether to recurse and generate refined workflow variants.

    At MVM stage, refinement is non-destructive and only annotates metadata.
    """

    def __init__(self, policy: Optional[RecursionPolicy] = None) -> None:
        self.policy = policy or RecursionPolicy()

    def should_recurse(self, depth: int, score_delta: float) -> bool:
        """
        Decide if another recursion step is warranted.

        Args:
            depth:
                Current recursion depth (0-based).
            score_delta:
                Improvement score compared to a previous version.

        Returns:
            True if we should recurse further, False otherwise.
        """
        if depth >= self.policy.max_depth:
            return False
        return score_delta >= self.policy.min_improvement

    def refine_workflow(
        self,
        workflow_data: Dict[str, Any],
        evaluation_report: Dict[str, Any],
        depth: int,
    ) -> Dict[str, Any]:
        """
        Create a minimally adjusted copy of workflow_data for the next recursion step.

        For the MVM, this simply attaches recursion metadata and returns a
        shallow copy of the input workflow.
        """
        refined_workflow = dict(workflow_data)
        recursion_metadata = refined_workflow.setdefault("recursion_metadata", {})
        recursion_metadata["depth"] = depth
        recursion_metadata["last_evaluation"] = evaluation_report
        return refined_workflow


def simple_refiner(workflow: Dict[str, Any]) -> Dict[str, Any]:
    """
    Minimal, MVM-friendly refinement wrapper.

    - Uses the local RecursionManager to attach recursion metadata.
    - Supplies safe defaults for evaluation_report and depth.
    - If the RecursionManager API changes or refinement fails, logs a warning
      and returns the original workflow unchanged.

    This ensures the MVM pipeline can rely on refinement being non-fatal.
    """
    # Instantiate the local RecursionManager with default policy.
    manager = RecursionManager()

    # Default evaluation report + depth for MVM stage.
    empty_report: Dict[str, Any] = {}
    depth = 0

    try:
        refined = manager.refine_workflow(workflow, empty_report, depth)
    except TypeError as exc:
        # Signature mismatch or unexpected parameters → soft fail
        logger.warning(
            "Refinement skipped in simple_refiner due to signature mismatch: %s",
            exc,
        )
        return workflow
    except Exception as exc:  # pylint: disable=broad-exception-caught
        # Any other refinement error should not break the MVM pipeline
        logger.warning("Refinement failed in simple_refiner: %s", exc)
        return workflow

    if not isinstance(refined, dict):
        logger.warning(
            "Refinement returned non-dict (%s); returning original workflow.",
            type(refined),
        )
        return workflow

    return refined
