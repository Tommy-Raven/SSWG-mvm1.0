#!/usr/bin/env python3
# scripts/write_git_REST_API_md.py
# Recursive_Grimoire_ v1.13.0 — GitHub REST API Documentation Generator
# Run manually or via the GitHub Action in .github/workflows/add_git_REST_API.yml

import os
from datetime import datetime

def main():
    content = f"""# 🧩 git_REST_API.md
### Recursive_Grimoire_ — GitHub REST API Integration Guide  
*(Version 1.0.0 — maintained under zencoder.alwaysIncludedRules)*

---

## 🧭 Overview
This document defines how Recursive_Grimoire_ interacts with GitHub’s REST API for:
- Automated commits, pull requests, and synchronization
- Recursive self-updates triggered by workflow generation events
- Secure token handling for self-evolving repositories

All API operations follow GitHub’s REST API v3 conventions.

Reference: https://docs.github.com/en/rest

---

## ⚙️ Endpoint Usage Examples

### Retrieve repository contents
```http
GET /repos/{{owner}}/{{repo}}/contents/{{path}}
Example:

bash
Copy code
curl -H "Authorization: token $GITHUB_TOKEN" \\
     https://api.github.com/repos/Tommy-Raven/AI_instructions_workflow/contents/ai_core/
Purpose:

Fetches file tree for versioning or diff generation.

Used by ai_core/evolution_tracker.py and meta-agents.

Create or update a file
http
Copy code
PUT /repos/{{owner}}/{{repo}}/contents/{{path}}
Example body:

json
Copy code
{{
  "message": "Auto-commit: update generated workflow",
  "content": "bXkgZmlsZSBjb250ZW50",  
  "branch": "main",
  "sha": "previous-file-sha"
}}
