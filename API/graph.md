# 🔗 Dependency Graph API (ai_graph/)  
### Graph Construction, Validation & Autocorrect

---

# 🌐 Class: `DependencyGraph`

### Constructor:
```python
dg = DependencyGraph(modules)
```

### Key Methods

#### `detect_cycle() -> bool`
Detects if the workflow DAG contains a cycle.

#### `autocorrect_missing_dependencies()`
Adds nodes/edges where needed.

#### `attempt_autocorrect_cycle()`
Tries to break cycles automatically.

---

# 📈 Export

Used by `ai_visualization` to generate:

- Mermaid graphs  
- Graphviz `.dot` files
