# Quickstart Guide

Welcome to **AI Instructions Workflow Generator v4.5**

This system creates, evaluates, and recursively evolves instructional AI workflows, providing both human- and machine-readable outputs.

---

## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/Tommy-Raven/AI_instructions_workflow.git
cd AI_instructions_workflow
```

2. **Install dependencies**

```bash
pip install -r REQUIREMENTS.txt
```

3. **Run the main generator**

```bash
python generator/main.py
```

4. **Trigger recursion (optional)**

When prompted, type `E` to generate recursive workflow variants and merge best results.

---

## 🛠 Requirements

* Python 3.11+
* VS Code recommended for editing, debugging, and testing
* Optional: Docker for containerized execution

---

## 📂 Outputs

* Human-readable: Markdown (`.md`)
* Machine-readable: JSON (`.json`)

All outputs are archived and versioned in `data/outputs/`.

---

## 🏗 Architecture Reference (`ARCHITECTURE.md`)

**AI Instructions Workflow v4.5** follows a modular, recursive design divided into eight optimization phases.

### 🔧 Core Directories

| Directory           | Purpose                                                              |
| ------------------- | -------------------------------------------------------------------- |
| `generator/`        | CLI & workflow creation, recursion management, caching, export logic |
| `ai_core/`          | Phase orchestration, dependency graph, task coordination             |
| `ai_recursive/`     | Variant generation, merging, memory tracking, and version evolution  |
| `ai_evaluation/`    | Workflow scoring, semantic comparison, quality metrics               |
| `ai_monitoring/`    | Logging, telemetry, real-time CLI dashboard                          |
| `ai_validation/`    | Schema validation, regression tests, version tracking                |
| `ai_visualization/` | Workflow graph rendering via Graphviz/Mermaid                        |
| `ai_memory/`        | Persistent storage, benchmarks, analytics, and feedback adaptation   |
| `ai_graph/`         | Dependency mapping and semantic network construction                 |

---

### 🔄 Workflow Phases

1. **Initialization & Variable Acquisition** — Gather inputs and environment variables
2. **Objective Refinement** — Convert abstract goals into measurable outcomes
3. **Human-Readable How-To Generation** — Generate Markdown/JSON instructions
4. **Modular Expansion & Reusability** — Create reusable workflow components
5. **Evaluation & Quality Assurance** — Semantic scoring, clarity, coverage, and AI-readability
6. **Regeneration & Evolution** — Recursive output refinement and feedback integration
7. **Visualization & Monitoring** — Render workflow graphs and track metrics
8. **Adaptive Optimization & Learning Memory** — Store and leverage prior run data for future improvements

---

### ⚡ Quick Tips

* Use `generator/main.py` for local CLI execution
* Recursive workflow generation improves clarity and reduces redundant steps
* All generated outputs are versioned in `data/outputs/` for traceability
* Combine with `ai_monitoring.telemetry` to track real-time recursion metrics

---

This Quickstart provides enough to generate your first workflow, monitor its evaluation, and optionally trigger recursive improvements for self-evolving workflows.
