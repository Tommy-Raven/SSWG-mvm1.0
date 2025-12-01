# Configuration Reference — Recursive_Grimoire_ v1.13.0

## Overview

This document outlines configuration files, environment settings, and schema references for **Recursive_Grimoire_**. Proper configuration ensures deterministic execution, reproducibility, and safe workflow generation.

---

## Configuration Files

| File                 | Purpose                                       |
| -------------------- | --------------------------------------------- |
| `requirements.txt`   | Python dependencies                           |
| `pyproject.toml`     | Build and packaging configuration             |
| `.editorconfig`      | Code formatting standards                     |
| `.gitignore`         | File exclusion for version control            |
| `config/` (optional) | Runtime, environment, and path configurations |

---

## JSON Schemas

| Schema                           | Description                                                              |
| -------------------------------- | ------------------------------------------------------------------------ |
| `schemas/workflow_schema.json`   | Defines structure, required fields, and dependencies for workflows       |
| `schemas/module_schema.json`     | Validates individual modules for naming, inputs, and outputs             |
| `schemas/evaluation_schema.json` | Ensures evaluation metrics and feedback loops conform to expected format |

---

## Environment Variables

* `RECURSIVE_MODE` — Enables recursive expansion on workflow generation
* `MEMORY_PATH` — Path to persistent memory storage (`ai_memory/`)
* `LOG_LEVEL` — Logging verbosity (`INFO`, `DEBUG`, `WARNING`, `ERROR`)
* `API_HOST` — Host for FastAPI endpoints
* `API_PORT` — Port for FastAPI endpoints

---

## Onboarding Highlights

* Each workflow phase may read configuration files for parameterization.
* JSON schema validation ensures module and workflow integrity.
* Environment variables allow safe toggling of recursive execution and memory tracking.
* Recommended workflow: clone → configure environment → validate schemas → run CLI or API.
