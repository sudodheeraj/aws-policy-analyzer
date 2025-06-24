#!/bin/bash
# ==========================
# AWS Policy Analyzer Runner
# ==========================
echo
echo "🔍 AWS Policy Analyzer"
echo

# Export AWS credentials
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
export AWS_DEFAULT_REGION="us-east-1"

echo "✅ AWS environment variables set."
echo

# Try online version
echo "⚡️ Running online version..."
if python3 src/aws_policy_analyzer.py; then
    echo "✅ Done! Results saved as:"
    echo " - policy_report.md"
    echo " - policy_report.html"
    echo " - policy_report.csv"
    echo " - policy_report.xlsx"
else
    echo "❌ AWS online version failed. Running offline mock version..."
    python3 src/aws_policy_analyzer_mock.py
    echo "✅ Done! Results saved from mock version."
fi
