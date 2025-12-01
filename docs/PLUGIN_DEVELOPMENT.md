# Plugin Development Guide — Extended

Plugins allow developers to extend **Recursive_Grimoire** without modifying core files. They can provide new evaluation metrics, workflow transformations, or integration hooks.

## Plugin Structure

```python
# Example: custom_plugin.py
from generator.plugin_loader import register_plugin

@register_plugin(name="CustomMetric")
def custom_quality_metric(workflow):
    """
    Compute a custom quality metric for a workflow.
    Returns a dictionary with metric values.
    """
    # Example computation
    score = len(workflow.steps) / 10
    return {"custom_score": score}
```

## How to Load Plugins

Define your plugins in the configuration file:

```yaml
# config/settings.yml
plugins:
  - custom_plugin
  - another_plugin
```

The system will automatically import and register each plugin at startup. Plugins can hook into:

* Evaluation cycles (`ai_evaluation`)
* Recursive expansions (`ai_recursive`)
* Workflow generation phases (`ai_core/phases`)

## Development Guidelines

* **Isolation:** Plugins must not modify core module logic.
* **Idempotence:** Ensure repeated calls produce consistent results.
* **Documentation:** Include docstrings and example usage.
* **Error Handling:** Catch exceptions and log errors without halting workflow execution.
* **Versioning:** Track plugin versions for compatibility with recursive workflows.

## Testing Plugins

* Place tests in `/tests/plugins/` following standard pytest conventions.
* Validate outputs against known workflows.
* Use semantic and benchmark scoring to ensure plugin metrics align with system goals.

## Example: Custom Workflow Transformer

```python
from generator.plugin_loader import register_plugin

@register_plugin(name="StepNormalizer")
def normalize_steps(workflow):
    """
    Adjust step formats and numbering for consistency.
    """
    for i, step in enumerate(workflow.steps):
        step["id"] = i + 1
        step["text"] = step["text"].strip()
    return workflow
```

This plugin can automatically standardize all workflow steps before evaluation or export.

---

## Next Steps

* Add more plugin hooks for FastAPI endpoints.
* Enable plugin-specific configuration via `settings.yml`.
* Consider sandboxing for untrusted plugin execution.
