# generator/async_executor.py
"""
Asynchronous Task Executor for SSWG MVM.
Provides helpers for running synchronous and asynchronous functions concurrently.
"""

from __future__ import annotations
import asyncio
import logging
from typing import Any, Awaitable, Callable, Coroutine, Iterable, List, Union

# ─── Logger Setup ──────────────────────────────────────────────
logger = logging.getLogger("async_executor")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)

# ─── Types ────────────────────────────────────────────────────
AsyncTaskType = Union[Callable[..., Awaitable[Any]], Coroutine[Any, Any, Any]]


# ─── Core Functions ───────────────────────────────────────────
async def run_task(task: AsyncTaskType, *args, **kwargs) -> Any:
    """
    Run a single asynchronous task (function or coroutine object) with logging.
    """
    try:
        if callable(task):
            result = await task(*args, **kwargs)
        else:
            result = await task
        return result
    except Exception as e:
        logger.error("Task %s failed: %s", getattr(task, "__name__", str(task)), e)
        return None


async def run_tasks_concurrently(
    tasks: Iterable[AsyncTaskType], *args, **kwargs
) -> List[Any]:
    """
    Run multiple async tasks concurrently.
    """
    coros: List[Coroutine[Any, Any, Any]] = []
    for t in tasks:
        if callable(t):
            coros.append(t(*args, **kwargs))
        else:
            coros.append(t)

    results = await asyncio.gather(*coros, return_exceptions=True)
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            logger.error("Task #%d failed during concurrent execution: %s", i, r)
            results[i] = None
    return results


# ─── Synchronous Helpers ──────────────────────────────────────
def run_sync(task: AsyncTaskType, *args, **kwargs) -> Any:
    return asyncio.run(run_task(task, *args, **kwargs))


def run_all_sync(tasks: Iterable[AsyncTaskType], *args, **kwargs) -> List[Any]:
    return asyncio.run(run_tasks_concurrently(tasks, *args, **kwargs))
