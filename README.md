# Recursive_Grimoire_ v1.13.0

## AI Instructional Workflow Generator

![Project Status: Experimental](https://img.shields.io/badge/status-experimental-orange) ![Python](https://img.shields.io/badge/language-Python-blue) ![Codename: Grimoire](https://img.shields.io/badge/codename-Grimoire-purple) ![License: Proprietary](https://img.shields.io/badge/license-Proprietary-lightgrey)

---

## Table of Contents

1. Overview
2. Design Philosophy
3. System Architecture
4. Core Features
5. How It Works
6. Example Templates
7. Operational Workflow
8. Intended Users
9. Technology Stack
10. Setup & Usage
11. Onboarding & Developer Guide
12. Future Enhancements
13. Contributing
14. License
15. Contact

---

# Overview

**Recursive_Grimoire_ v1.13.0** is a **meta-educational AI system** that conjures, evaluates, and evolves **instructional workflows** automatically. It functions both as a *teacher* and a *scribe*, translating user intent into self-contained learning frameworks that recursively generate new instructions for humans or AI agents. Each workflow is a **grimoire of knowledge**, structured with packages for modules, tasks, dependencies, and logic sequences, capable of **recursive self-expansion**, meaning it can learn from its own output, and capable of teaching other AI systems as well.

The updated SSWG is a modular system for generating, evaluating, and publishing structured workflows from high-level user goals. It includes:

* Goal parsing and clarification
* Workflow generation & evaluation
* Constitution & safety enforcement
* Contradiction detection & auto-remediation
* Risk assessment
* Deterministic execution & reproducibility
* FastAPI-based web interface
* Unit, integration, and acceptance testing
* CI/CD workflows

---

# Design Philosophy

> "Each workflow teaches the next workflow how to teach."

The design philosophy emphasizes the iterative nature of the system. Each generated workflow is not just a static product but a stepping stone for the next, continuously refining the teaching process. This is achieved through the system's ability to learn from its own outputs, adapt to new information, and evolve its instructional strategies.

Ancient grimoire inspiration adds depth, suggesting that the system incorporates knowledge preservation, symbolic representation, and recursive meta-learning. The end result is workflows that are both effective and adaptable, capable of generating new knowledge and improving pedagogical approaches over time.

---

# System Architecture

The system is organized in **layers** with clear separation of concerns:

**Core** – Configuration, logging, exceptions
**Parsing** – Extract intents from user goals; generate clarifications; validate schemas
**Constitution Engine** – Apply rules and predicates to approve or reject workflows
**Contradiction Detector** – Identify inconsistencies; auto-remediate when possible
**Safety Stack** – Sanitize inputs/outputs; assess safety; sandbox simulation
**Agents** – GeneratorAgent, EvaluatorAgent, EvolutionEngine, Archivist
**Risk Pipeline** – Weighted scoring of workflow steps
**Reproducibility** – DeterministicRunner, Reconstruct API, model metadata tracking
**Web Layer** – FastAPI routes for workflows, runs, inventory
**Testing & CI** – Unit, integration, acceptance tests; GitHub Actions workflow

**Root-Level Files** include configuration, dependency management, legal, and documentation for contributors. Supporting folders handle templates, generated workflows, modules, schemas, meta-knowledge, data storage, visualization, monitoring, and optional containerization.

---

# Core Features

* Recursive Workflow Generation — Every output can seed future workflows
* Bimodal Representation — Markdown for humans; minified JSON for machines
* Dependency Graph DAG — Visualizes module interconnections; avoids conflicts
* Schema-Driven Validation — Maintains logical consistency across all phases
* Persistent Memory System — Archives outputs with full version history
* Self-Evaluative Feedback Loop — Measures clarity, coverage, AI translatability
* Visual Export — Graphviz diagrams for human inspection
* Structured Logging — Tracks all generation events
* Optional Arcane-Themed Modules (~30% of workflow modules)

---

# How It Works

1. Invocation — User specifies workflow purpose, audience, and style
2. Phase Generation — Constructs a six-phase workflow:

   * Phase 1: Initialization & Variable Acquisition
   * Phase 1.5: Objective Refinement (abstract → measurable goals)
   * Phase 2: Human-Readable How-To Generation
   * Phase 3: Modular Expansion & Reusability
   * Phase 4: Evaluation & Quality Assurance
   * Phase 5: Regeneration & Evolution
3. Validation — Schema verification ensures completeness, dependency integrity, and uniqueness
4. Evaluation — Metrics measure clarity, coverage, expansion potential, and AI translatability
5. Reflection & Regeneration — Versioning, minified JSON export, recursive self-improvement

---

# Example Templates

| Template                          | Focus         | Primary Use                              |
| --------------------------------- | ------------- | ---------------------------------------- |
| training_curriculum_template.json | Education     | Build structured learning programs       |
| technical_procedure_template.json | Engineering   | Standardize technical workflows          |
| creative_writing_template.json    | Arts          | Generate literary or narrative workflows |
| meta_reflection_template.json     | Metacognition | Evaluate and evolve cognitive frameworks |

---

# Operational Workflow

The system supports **recursive execution** and **feedback loops** across all workflow phases, allowing continuous self-improvement and modular expansion.

---

# Intended Users

* AI Developers — Explore recursive instructional AI
* Educators & Trainers — Auto-generate curriculum structures
* Writers & Designers — Create recursive creative frameworks
* Research Institutions — Investigate AI-guided pedagogy and meta-learning

---

# Technology Stack

* Python 3.10+
* JSON + Markdown hybrid architecture
* Graphviz (optional) for visualization
* pytest for validation testing
* Custom AI reasoning modules (planned)

---

# Setup & Usage

Clone Repository:
git clone [https://github.com/Tommy-Raven/AI_instructions_workflow.git](https://github.com/Tommy-Raven/AI_instructions_workflow.git)
cd AI_instructions_workflow

Install Dependencies:
pip install -r requirements.txt

Run CLI:
python cli.py --purpose "Design an AI ethics curriculum"

View Results:

* Generated JSON: `data/workflows/`
* Logs: `logs/workflow.log`
* Optional Graph: `build/workflow_graph.dot`

---

# Onboarding & Developer Guide

* **Folder Structure** — Understand modular layers: ai_core, ai_recursive, ai_memory, ai_evaluation
* **Templates & Schemas** — Use `data/templates/` and `schemas/` for validation
* **Agents & Engines** — GeneratorAgent, EvaluatorAgent, EvolutionEngine, Archivist
* **Testing** — Use pytest to run unit, integration, and acceptance tests
* **CI/CD** — GitHub Actions workflow preconfigured for build, test, and deployment
* **Contribution Flow** — Submit pull requests; follow coding standards in CONTRIBUTOR_GUIDE.md

---

# Future Enhancements

* Adaptive semantic embeddings for self-learning
* Domain-specific plugin grimoires
* Multi-agent recursive co-generation
* Interactive dashboard visualization
* Open LLM integration for semantic workflow synthesis
* Automatic derivative workflow generation with lineage tracking

---

# Contributing

See CONTRIBUTOR_GUIDE.md for details. Submit issues or pull requests via GitHub.

---

# License

Proprietary — Research Phase
All rights reserved © 2025 Tommy Raven / Raven Recordings

---

# Contact

* Author: Tommy Raven
* Email: GitHub Issues preferred
* Codename: Recursive_Grimoire_ v1.13.0
* Repository: github.com/Tommy-Raven/AI_instructions_workflow
