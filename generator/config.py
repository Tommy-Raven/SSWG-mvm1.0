#!/usr/bin/env python3
"""
generator/config.py — Configuration Management for SSWG
Modernized, type-checked, and fully async-compatible.
"""

from __future__ import annotations
import json
import asyncio
from pathlib import Path
from typing import Any, Dict, Optional


class ConfigManager:
    """Async-aware configuration manager for loading and saving workflow settings."""

    def __init__(
        self,
        config_path: Optional[Path] = None,
        default_config: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Args:
            config_path (Optional[Path]): Path to JSON configuration file. If None, config is in-memory only.
            default_config (Optional[Dict[str, Any]]): Default configuration to initialize if file is missing.
        """
        self.config_path = config_path
        self.config: Dict[str, Any] = default_config or {}

    async def load(self) -> None:
        """Load configuration from JSON file asynchronously."""
        if self.config_path is None or not self.config_path.exists():
            return

        loop = asyncio.get_running_loop()
        content = await loop.run_in_executor(None, self.config_path.read_text)
        self.config = json.loads(content)

    async def save(self) -> None:
        """Save current configuration to JSON file asynchronously."""
        if self.config_path is None:
            return

        loop = asyncio.get_running_loop()
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        await loop.run_in_executor(
            None, self.config_path.write_text, json.dumps(self.config, indent=2)
        )

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Retrieve a configuration value.

        Args:
            key (str): Configuration key.
            default (Optional[Any]): Default value if key is missing.

        Returns:
            Any: Value from config or default.
        """
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.

        Args:
            key (str): Configuration key.
            value (Any): Value to store.
        """
        self.config[key] = value


#
