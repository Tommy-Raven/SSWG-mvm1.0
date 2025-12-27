---
anchor:
  anchor_id: performance_benchmarks_doc
  anchor_version: 1.0.0
  scope: docs
  owner: docs.performance
  status: draft
---

# Performance Benchmarks

This document tracks memory usage, recursion time, module reuse, and throughput efficiency across workflow generations. Benchmarks are used to guide optimization, ensure deterministic execution, and evaluate system evolution.

## ✅ Latest Measured Results (2025-12-27T09:07:21Z)

**Raw results:** [`artifacts/performance/benchmarks_20251227_090721.json`](../artifacts/performance/benchmarks_20251227_090721.json)

### Environment Metadata

| Field | Value |
| --- | --- |
| OS | Linux-6.12.13-x86_64-with-glibc2.39 |
| Kernel | 6.12.13 |
| Machine | x86_64 |
| CPU | Intel(R) Xeon(R) Platinum 8370C CPU @ 2.80GHz (3 cores available) |
| Memory | 19,253,211,136 bytes (~17.9 GiB) |
| Python | 3.11.12 |

### Dataset + Reminder

| Field | Value |
| --- | --- |
| Dataset | `pdl/example_full_9_phase.yaml` |
| Size | 3,678 bytes (135 lines) |
| SHA-256 | `452e1190af820d3f9a552a4adc6535e1db7b15694b0d0ede290816c0e06c2acc` |

### Run Configuration

| Setting | Value |
| --- | --- |
| IO read iterations | 2,000 |
| IO write iterations | 500 |
| Phase timing iterations | 200 |
| Recursion iterations | 50 |

### Throughput (Measured)

| Metric | Value |
| --- | --- |
| IO read throughput | 557.30 MB/s |
| IO write throughput | 28.57 MB/s |
| IO read elapsed | 0.0126 s |
| IO write elapsed | 0.0614 s |

### Phase Completion Time (Average per iteration)

| Phase | Average (s) | Total (s) |
| --- | --- | --- |
| normalize | 0.00001319 | 0.0026 |
| parse | 0.00834265 | 1.6685 |
| analyze | 0.00000083 | 0.0002 |
| generate | 0.00000646 | 0.0013 |
| validate | 0.00663457 | 1.3269 |
| compare | 0.00000012 | 0.0000 |
| interpret | 0.00000033 | 0.0001 |
| log | 0.00003990 | 0.0080 |

### Recursion Timing

| Metric | Value |
| --- | --- |
| Total recursion time (50 iterations) | 0.7292 s |
| Average per recursion iteration | 0.0146 s |

## 🧠 Benchmark Metrics

| Metric                | Description                                                    | Notes                                                                 |
| --------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------- |
| Recursion Time        | Total runtime per generation cycle                             | Measured from workflow initialization to final output persistence     |
| Cache Hits            | Number of reused modules or workflows                          | Indicates efficiency of modularization and memory reuse               |
| Memory Usage          | RAM consumption in MB                                          | Includes active data, memory store, and evaluation overhead           |
| Semantic Stability    | Average delta between iterations                               | Helps determine when recursion output has stabilized                  |
| IO Throughput         | Reads/writes per workflow cycle                                | Tracks template and output handling performance                       |
| Phase Completion Time | Per-phase runtime                                              | Identifies bottlenecks in initialization, evaluation, or regeneration |
| Evaluation Overhead   | Runtime of clarity, expandability, and translatability scoring | Monitors impact of metric calculations on total cycle                 |

## 📊 Recording & Reporting

* Benchmarks are collected in `ai_memory/benchmark_tracker.py`.
* Data is logged with timestamps, version IDs, and phase markers.
* CLI dashboard and visualization tools display performance trends.
* Metrics support adaptive optimization, such as caching strategies, async execution, and semantic delta stopping.

## 📌 Profiling Snapshots (2025-12-27)

**Methodology**

* Workloads: `campfire_workflow.json` and `technical_procedure_template.json` from `data/templates/`.
* Phases measured: load workflow, normalize task packaging, inheritance checks, schema validation, dependency graph build, mermaid render, evaluation scoring, meta metrics, and export artifacts.
* Timing: `time.perf_counter()` per phase.
* Memory: `tracemalloc` per phase (reported in KiB; captures Python allocation peaks).
* Schema validation attempts may include remote `$ref` resolution; the snapshot records any validation exception text.

**Artifacts**

* Snapshot JSON: [`data/profiling/workflow_profiling_2025-12-27.json`](../data/profiling/workflow_profiling_2025-12-27.json)
* Campfire outputs:
  * [`data/profiling/campfire_workflow/campfire_workflow.json`](../data/profiling/campfire_workflow/campfire_workflow.json)
  * [`data/profiling/campfire_workflow/campfire_workflow.md`](../data/profiling/campfire_workflow/campfire_workflow.md)
* Technical procedure outputs:
  * [`data/profiling/technical_procedure_template/unnamed_workflow.json`](../data/profiling/technical_procedure_template/unnamed_workflow.json)
  * [`data/profiling/technical_procedure_template/unnamed_workflow.md`](../data/profiling/technical_procedure_template/unnamed_workflow.md)

## ⚡ Optimization Integration

* Core stability and exception handling minimize runtime errors and infinite loops.
* Semantic intelligence and delta scoring inform adaptive recursion termination.
* Memory caching and garbage collection reduce overhead for large workflow sets.
* Multithreaded execution increases throughput for parallel workflow generation.
* Persistent memory analytics support long-term performance improvements.
