import json

def analyze_policy(document):
    """Check a policy document for wildcard permission."""
    findings = []
    for statement in document.get('Statement', []):
        if isinstance(statement, dict): 
            statements = [statement]
        else:
            statements = statement
        for stmt in statements:
            action = stmt.get('Action', '')
            resource = stmt.get('Resource', '')
            if action == '*' or resource == '*':
                findings.append({
                    'Statement': stmt,
                    'Risk': 'High',
                    'Reason': 'Wildcard permission detected'
                })
    return findings

if __name__ == '__main__':
    mock_policies = [
        {
            "PolicyName": "TestRiskyPolicy",
            "PolicyArn": "arn:aws:iam::123456789012:policy/TestRiskyPolicy",
            "PolicyDocument": {
                "Statement": [
                    {"Effect": "Allow", "Action": "*", "Resource": "*"},
                    {"Effect": "Allow", "Action": "ec2:DescribeInstances", "Resource": "*"}
                ]
            }
        },
        {
            "PolicyName": "SafePolicy",
            "PolicyArn": "arn:aws:iam::123456789012:policy/SafePolicy",
            "PolicyDocument": {
                "Statement": [
                    {"Effect": "Allow", "Action": "ec2:DescribeInstances", "Resource": "*"}
                ]
            }
        }
    ]

    results = []
    for p in mock_policies:
        findings = analyze_policy(p["PolicyDocument"])
        if findings:
            results.append({
                "PolicyName": p["PolicyName"],
                "PolicyArn": p["PolicyArn"],
                "Findings": findings
            })

    if results:
        print("\n🚩 Risky Policies Found:\n")
        print(json.dumps(results, indent=4))
    else:
        print("\n✅ No risky policies found.")
