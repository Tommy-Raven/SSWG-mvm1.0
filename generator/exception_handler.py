#!/usr/bin/env python3
"""
generator/exception_handler.py — Centralized Exception Handling for SSWG
Modernized, type-annotated, async-compatible.
"""

from __future__ import annotations
import logging
import traceback
from typing import Callable, Any, Optional, Type

logger = logging.getLogger("generator.exception_handler")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)


def handle_exceptions(
    func: Callable[..., Any],
    *,
    default_return: Optional[Any] = None,
    log_traceback: bool = True,
) -> Callable[..., Any]:
    """
    Decorator to wrap functions in a try/except block, logging exceptions.

    Args:
        func (Callable[..., Any]): Function to wrap.
        default_return (Optional[Any], optional): Return value if exception occurs. Defaults to None.
        log_traceback (bool, optional): Whether to log full traceback. Defaults to True.

    Returns:
        Callable[..., Any]: Wrapped function.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error("Exception in %s: %s", func.__name__, e)
            if log_traceback:
                tb = traceback.format_exc()
                logger.debug(tb)
            return default_return

    return wrapper


async def async_handle_exceptions(
    coro_func: Callable[..., Any],
    *,
    default_return: Optional[Any] = None,
    log_traceback: bool = True,
) -> Callable[..., Any]:
    """
    Wrap an async coroutine function to safely catch exceptions.

    Args:
        coro_func (Callable[..., Any]): Async function to wrap.
        default_return (Optional[Any], optional): Value to return on exception. Defaults to None.
        log_traceback (bool, optional): Whether to log full traceback. Defaults to True.

    Returns:
        Callable[..., Any]: Async wrapper function.
    """

    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return await coro_func(*args, **kwargs)
        except Exception as e:
            logger.error("Async exception in %s: %s", coro_func.__name__, e)
            if log_traceback:
                tb = traceback.format_exc()
                logger.debug(tb)
            return default_return

    return wrapper
