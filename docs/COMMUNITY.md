# Community & Collaboration Guide

## Overview

**Recursive_Grimoire_ v1.13.0** encourages collaboration, learning, and shared development of AI instructional workflows. This document outlines community expectations, contribution paths, and communication channels.

---

## Getting Started

* **Explore the repository** — Review `README.md`, `docs/`, and example workflows in `data/templates/`.
* **Clone the repo** — `git clone https://github.com/Tommy-Raven/AI_instructions_workflow.git`
* **Install dependencies** — `pip install -r requirements.txt`
* **Run tests** — `pytest tests/` to ensure your environment is working.

---

## Contribution Guidelines

* Submit bug reports or feature requests via GitHub Issues.
* Fork the repository for development; create a feature branch for your changes.
* Follow the phase-based workflow structure when adding modules or templates.
* Ensure any new workflows are validated against JSON schemas (`schemas/`).
* Include unit tests for all new functionality in `tests/`.
* Pull Requests should reference the issue, provide a clear description, and pass CI checks.

---

## Code of Conduct

* Respect all community members.
* Keep discussions focused on ideas and solutions.
* Avoid sharing sensitive information or proprietary content.
* Follow best practices for secure AI development.

---

## Communication Channels

* **GitHub Issues & Pull Requests** — Primary discussion and contribution forum.
* **Docs & Wiki** — Reference `docs/` for architecture, API, and recursive workflow guides.
* **Discussions / Q&A** — Use GitHub Discussions for brainstorming and non-urgent questions.

---

## Onboarding Highlights

* Each module is designed for clarity: initialization → refinement → generation → evaluation → regeneration.
* Recursive outputs teach subsequent workflows, creating an evolving knowledge base.
* JSON and Markdown outputs are human- and machine-readable.
* Use `generator/main.py` or FastAPI endpoints to explore recursive workflow creation.