# AI Instructional Workflow Generator — System Architecture

## Overview

This document outlines the architecture of **Recursive_Grimoire_ v1.13.0**, a modular AI system for generating, evaluating, and recursively improving instructional workflows. The system supports human- and machine-readable outputs, persistent memory, recursive feedback loops, and deterministic execution. The architecture emphasizes clear modular separation, recursive workflow design, and integration with safety, constitution, and risk pipelines.

---

## Layers and Modules

### Root / Project Base

* Configuration, environment, and standard project files
* `.editorconfig`, `.gitignore`, `README.md`, `CHANGELOG.md`, `LICENSE`
* Dependency management: `pyproject.toml`, `REQUIREMENTS.txt`
* Packaging instructions: `make_repo_zip_instructions.txt`

### Interface / Legacy CLI

* `/generator/` — CLI scripts for workflow invocation
* Modules: `main.py`, `workflow.py`, `evaluation.py`, `recursive_expansion.py`, `exporters.py`, `utils.py`
* Entry points for initiating workflow generation and recursive expansion

### Core Orchestration — `ai_core/`

* Handles workflow logic, module management, and recursive control
* Subpackages and modules:

  * `phases/` — Initialization, Objective Refinement, Modularization, Human-Readable Generation, Evaluation, Regeneration
  * `workflow.py` — Main orchestration engine
  * `registry.py` — Central storage of workflow metadata

### Recursive Engine — `ai_recursive/`

* Expansion engine: generates new workflows from previous outputs
* Merging engine: resolves conflicts and consolidates workflows
* Evaluator: scores recursive outputs for clarity, coverage, and translatability
* Registry and memory interfaces: track lineage and versioning

### Memory System — `ai_memory/`

* Stores workflows, versioned histories, metrics, and analytics
* Provides persistent storage for traceable recursive iterations

### Evaluation — `ai_evaluation/`

* Assesses workflow quality, clarity, coverage, and AI-readability
* Provides structured feedback for recursive improvement

### Supporting Data & Schemas — `data/`, `schemas/`

* Templates: standardized JSON/Markdown formats for workflows
* Outputs: generated workflows for human and machine consumption
* JSON schemas: enforce structure, dependencies, and consistency

### Safety Stack

* `safety/` modules: sanitizers, safety classifiers, sandbox simulation
* Ensures safe and policy-compliant workflow outputs

### Constitution Engine — `constitution/`

* Enforces rules and predicates from a rulebook
* Approves, rejects, or flags workflows for logical consistency

### Contradiction Detection & Auto-Remediation — `contradiction/`

* Identifies inconsistencies such as draft vs approved conflicts
* Automatically resolves contradictions where possible

### Reproducibility & Deterministic Execution — `reproducibility/`

* `DeterministicRunner`: stable execution via hashing and canonicalization
* Reconstruct API and model metadata tracking ensure repeatable results

### Web Layer — `web/`

* FastAPI endpoints for workflows, runs, and inventory
* RESTful interface for triggering workflow generation and evaluation

### Testing & CI — `tests/`

* Unit, integration, and acceptance tests
* GitHub Actions workflows for CI/CD automation

---

## Onboarding Highlights

* Each workflow teaches the next workflow how to teach
* Recursive loops ensure continuous improvement and evolution
* Modular structure supports clear phase-based progression
* Outputs are versioned, archived, and fully traceable
* Integration-friendly with safety, evaluation, and constitution pipelines

---

## Phase-Based Workflow Overview

1. **Initialization** — Variable acquisition and setup
2. **Objective Refinement** — Abstract goals → measurable outcomes
3. **Human-Readable How-To Generation** — Produce Markdown/JSON instructions
4. **Modular Expansion** — Generate reusable workflow modules
5. **Evaluation** — Clarity, coverage, and AI-readability scoring
6. **Regeneration & Evolution** — Recursive output and feedback integration

---

## Directory & File Mapping

* `ai_core/` — Orchestration and workflow phases
* `ai_recursive/` — Recursive generation, merging, memory, evaluation, registry
* `ai_memory/` — Persistent workflow storage and metrics
* `ai_evaluation/` — Quality assessment and feedback loops
* `generator/` — CLI and entry points
* `data/` — Templates and generated workflows
* `schemas/` — JSON schema validation
* `constitution/` — Rulebook enforcement
* `contradiction/` — Conflict detection and auto-remediation
* `reproducibility/` — Deterministic execution
* `safety/` — Sanitization, classification, sandbox simulation
* `web/` — FastAPI interface
* `tests/` — Automated testing

---

## Design Principles

* **Modularity:** Clear separation of orchestration, evaluation, validation, memory, and visualization
* **Recursive Design:** Self-learning workflows with iterative improvement
* **Traceable Outputs:** Versioned, archived, and human/machine-readable
* **Integration-Ready:** Seamless interaction with safety, constitution, and risk pipelines
* **Deployment-Ready:** CLI, containerization, and visualization support
