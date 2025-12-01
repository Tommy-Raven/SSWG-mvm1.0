# Telemetry & Logging — Updated

## Overview

Telemetry and structured logging provide real-time insight into workflow recursion, performance, and quality. Metrics are captured at each iteration and visualized via CLI dashboards or stored for historical analysis.

---

## 🧭 Modules

* `ai_monitoring/telemetry.py` — Collects runtime metrics from recursive workflows.
* `ai_monitoring/structured_logger.py` — Outputs structured JSON logs compatible with dashboards and analysis tools.
* `ai_monitoring/cli_dashboard.py` — Live terminal visualization for recursion depth, iteration speed, and quality metrics.

---

## 🧩 Metrics Tracked

* Recursion depth per workflow cycle
* Semantic delta score between iterations
* Workflow quality score (clarity, expandability, translatability)
* Memory usage (RAM consumption in MB)
* Generation time per cycle
* Cache hits and module reuse

---

## Example Log Format

```json
{
  "iteration": 3,
  "depth": 2,
  "semantic_score": 0.87,
  "quality_score": 9.1,
  "memory_mb": 212,
  "generation_time_sec": 14.5,
  "timestamp": "2025-11-03T16:00Z"
}
```

---

## Notes

* Logs integrate with `RecursionManager` to detect convergence and halt conditions.
* Historical logs can be analyzed for trend detection and performance tuning.
* Designed for both human readability and machine parsing for analytics pipelines.
