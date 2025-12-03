#!/usr/bin/env python3
"""
generator/cache_manager.py — Async-aware Cache Manager for SSWG
Modernized, type-checked, and fully asyncio compatible.
"""

from __future__ import annotations
import asyncio
from pathlib import Path
from typing import Any, Optional


class CacheManager:
    """Async-aware file cache manager for storing and retrieving workflow artifacts."""

    def __init__(self, storage_path: Optional[Path] = None) -> None:
        """
        Args:
            storage_path (Optional[Path]): Path to the cache file. If None, caching is disabled.
        """
        self.storage_path = storage_path

        if self.storage_path is not None:
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)

    async def save(self, data: str) -> None:
        """
        Save data to the cache asynchronously.

        Args:
            data (str): Serialized data to write.
        """
        if self.storage_path is None:
            return

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.storage_path.write_text, data)

    async def load(self) -> Optional[str]:
        """
        Load data from the cache asynchronously.

        Returns:
            Optional[str]: Cached content, or None if cache file does not exist.
        """
        if self.storage_path is None or not self.storage_path.exists():
            return None

        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self.storage_path.read_text)

    async def clear(self) -> None:
        """
        Clear the cache asynchronously.
        """
        if self.storage_path is None or not self.storage_path.exists():
            return

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.storage_path.unlink)
