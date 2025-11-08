git_REST_API.md
###Recursive_Grimoire_ — GitHub REST API Integration Guide  
*(Version 1.0.0 — maintained under zencoder.alwaysIncludedRules)*

---

## 🧭 Overview
This document defines how Recursive_Grimoire_ interacts with GitHub’s REST API for:
- Automated commits, pull requests, and synchronization
- Recursive self-updates triggered by workflow generation events
- Secure token handling for self-evolving repositories

All API operations follow GitHub’s REST API v3 conventions.

Reference: https://docs.github.com/en/rest


```
```
Endpoint Usage Examples

### Retrieve repository contents

GET /repos/{{owner}}/{{repo}}/contents/{{path}}

Example:
curl -H "Authorization: token $GITHUB_TOKEN" \\
     https://api.github.com/repos/Tommy-Raven/AI_instructions_workflow/contents/ai_core/
Purpose:

Fetches file tree for versioning or diff generation.

Used by ai_core/evolution_tracker.py and meta-agents.

### Create or update a file
PUT /repos/{{owner}}/{{repo}}/contents/{{path}}
Example body:
{{
  "message": "Auto-commit: update generated workflow",
  "content": "bXkgZmlsZSBjb250ZW50",  
  "branch": "main",
  "sha": "previous-file-sha"
}}
