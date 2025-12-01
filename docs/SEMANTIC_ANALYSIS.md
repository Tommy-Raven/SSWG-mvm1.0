# Semantic Analysis & Scoring

## Overview

The Semantic Analysis module evaluates recursive workflow outputs to determine meaningful changes and content stability. It integrates directly with the recursion manager to enforce stopping conditions when outputs converge.

---

## Purpose

* Detect whether new recursive outputs meaningfully differ from previous iterations.
* Assign delta and similarity scores using cosine similarity, Levenshtein distance, or embedding-based semantic metrics.
* Automatically halt recursion if semantic change falls below a configurable threshold.
* Provide actionable feedback for phase refinement and improvement.

---

## Scoring Formula

```
Semantic Delta = 1 - Similarity(Old_Output, New_Output)
```

Where `Similarity()` can be computed using text embeddings or token-level distance measures.

---

## Example Integration

```python
from generator.semantic_scorer import SemanticScorer

scorer = SemanticScorer()
score = scorer.compare(text_a, text_b)

if score < 0.15:
    stop_recursion()
```

---

## Notes

* Supports integration with `ai_evaluation` to log scores and track semantic stability over multiple iterations.
* Works with both human-readable Markdown workflows and machine-readable JSON outputs.
* Configurable thresholds allow fine-grained control over recursion halting conditions.
