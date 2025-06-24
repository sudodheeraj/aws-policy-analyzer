import pytest
import os
import sys

# Add parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.aws_policy_analyzer_mock import analyze_policy


def test_analyze_policy_wildcard():
    test_doc = {
        "Statement": [
            {"Effect": "Allow", "Action": "*", "Resource": "*"}
        ]
    }
    findings = analyze_policy(test_doc)
    assert len(findings) == 1
    assert findings[0]["Risk"] == "High"

def test_analyze_policy_safe():
    test_doc = {
        "Statement": [
            {"Effect": "Allow", "Action": "ec2:DescribeInstances", "Resource": "*"}
        ]
    }
    findings = analyze_policy(test_doc)
    assert len(findings) == 1  # ✅ Expect a finding