#!/usr/bin/env python3
"""
generator/evaluation.py — Evaluation Engine for SSWG
Modernized, type-checked, async-compatible.
"""

from __future__ import annotations
import asyncio
import logging
from typing import Any, Dict, Callable, List, Optional

logger = logging.getLogger("generator.evaluation")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)


class EvaluationEngine:
    """Handles evaluation of workflow phases, modular and async-friendly."""

    def __init__(self) -> None:
        self._evaluators: Dict[str, Callable[[Dict[str, Any]], Any]] = {}

    def register_evaluator(
        self, phase_name: str, func: Callable[[Dict[str, Any]], Any]
    ) -> None:
        """
        Register an evaluator function for a specific phase.

        Args:
            phase_name (str): Phase identifier.
            func (Callable[[Dict[str, Any]], Any]): Evaluation function.
        """
        self._evaluators[phase_name] = func
        logger.info("Registered evaluator for phase: %s", phase_name)

    async def evaluate_phase(self, phase_name: str, context: Dict[str, Any]) -> Any:
        """
        Evaluate a single phase asynchronously.

        Args:
            phase_name (str): Phase to evaluate.
            context (Dict[str, Any]): Context for evaluation.

        Returns:
            Any: Evaluation result.
        """
        evaluator = self._evaluators.get(phase_name)
        if not evaluator:
            logger.warning("No evaluator registered for phase: %s", phase_name)
            return None

        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, evaluator, context)

    async def evaluate_all(
        self, context: Dict[str, Any], phases: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Evaluate all registered phases or a subset asynchronously.

        Args:
            context (Dict[str, Any]): Workflow context.
            phases (Optional[List[str]]): Subset of phases to evaluate. Evaluates all if None.

        Returns:
            Dict[str, Any]: Mapping of phase_name -> evaluation result.
        """
        phases_to_eval = phases or list(self._evaluators.keys())
        results: Dict[str, Any] = {}

        for phase in phases_to_eval:
            result = await self.evaluate_phase(phase, context)
            results[phase] = result

        return results
