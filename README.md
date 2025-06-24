# AWS Policy Analyzer 🔍

Scan AWS IAM policies for **overly permissive rules** (`Action: "*"` or `Resource: "*"`).
✅ Export results to Markdown, HTML, CSV, and Excel.
✅ Works online (AWS) and offline (mock data).
✅ Scripts for one-command runs (`.bat` for Windows, `.sh` for Linux/macOS).

---

## ⚡️ Features

- Works with AWS (`boto3`) & Offline (no AWS required)
- Detects wildcard policies (`Action: "*"` or `Resource: "*"`)
- Export results to Markdown, HTML, CSV, and Excel
- Includes one-click shell scripts

---

## 🐍 Requirements

- **Python 3.9+**
- Install required packages:
  ```bash
  pip install boto3 openpyxl pytest
  ```

---

## 🗄️ Directory Layout

```
aws-policy-analyzer/
├─ src/
│  └─ aws_policy_analyzer.py           # Main script
│  └─ aws_policy_analyzer_mock.py      # Offline version
├─ examples/
├─ test/
├─ .gitignore
├─ run_tool.bat                      # Windows one-click script
├─ run_tool.sh                       # Linux/macOS one-click script
├─ README.md
```

---

## ⚡️ Usage

### ✅ 1️⃣ Online Version (With AWS Credentials)

#### Export AWS Credentials

Edit `.bat` or `.sh` files:

```
set AWS_ACCESS_KEY_ID=your-access-key
set AWS_SECRET_ACCESS_KEY=your-secret-access-key
set AWS_DEFAULT_REGION=us-east-1
```

(or run):

```
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
export AWS_DEFAULT_REGION="us-east-1"
```

#### Run

```
python src/aws_policy_analyzer.py
```

### ✅ 2️⃣ Offline Version (No AWS Needed)

```
python src/aws_policy_analyzer_mock.py
```

---

## ⚡️ Scripts

### 🪟 Windows

Edit `run_tool.bat` with your AWS keys, then run:

```
.\run_tool.bat
```

### 🐧 Linux / 🍏 macOS

Edit `run_tool.sh`:

```
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
export AWS_DEFAULT_REGION="us-east-1"
```

Make script executable:

```
chmod +x run_tool.sh
```

Run:

```
./run_tool.sh
```

---

## ✅ Output

Results saved as:

- `policy_report.md`
- `policy_report.html`
- `policy_report.csv`
- `policy_report.xlsx`

---

## 🧪 Testing

Run unit tests:

```
pytest
```
