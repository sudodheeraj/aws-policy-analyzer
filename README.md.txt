# AWS Policy Analyzer 🔍

Scan AWS IAM policies for **overly permissive** rules (`Action: "*"` or `Resource: "*"`).

✅ Works online & offline  
✅ Provides JSON Output  
✅ Enables quick security review

---

## ⚡️ Features
- Works with live AWS (boto3) & offline
- Detects wildcard policies
- Provides actionable output
- Includes test examples

---

## ⚡️ Usage
### Install Dependencies
```bash
pip install boto3 pytest
