import boto3
import json
import csv
from openpyxl import Workbook
import botocore.exceptions

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

def scan():
    """Scan AWS IAM for policies with wildcard permissions."""
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_policies')
    results = []
    for page in paginator.paginate(Scope='Local'):
        for policy in page['Policies']:
            version = iam.get_policy_version(
                PolicyArn=policy['Arn'], VersionId=policy['DefaultVersionId']
            )
            findings = analyze_policy(version['PolicyVersion']['Document'])
            if findings:
                results.append({
                    'PolicyName': policy['PolicyName'],
                    'PolicyArn': policy['Arn'],
                    'Findings': findings
                })
    return results

def export_to_markdown(results, filename="policy_report.md"):
    """Export results to a Markdown file."""
    with open(filename, "w") as f:
        f.write("# AWS Policy Analyzer Report\n\n")
        if results:
            for item in results:
                f.write(f"## Policy: {item['PolicyName']}\n\n")
                f.write(f"**Policy ARN:** `{item['PolicyArn']}`\n\n")
                for finding in item['Findings']:
                    statement = finding['Statement']
                    action = statement.get('Action', '')
                    resource = statement.get('Resource', '')
                    reason = finding.get('Reason', '')
                    risk = finding.get('Risk', '')
                    f.write(f"- Action: `{action}`\n")
                    f.write(f"- Resource: `{resource}`\n")
                    f.write(f"- Risk: **{risk}**\n")
                    f.write(f"- Reason: {reason}\n\n")
        else:
            f.write("✅ No risky policies found.\n")
    print(f"✅ Markdown report saved to: {filename}")

def export_to_html(results, filename="policy_report.html"):
    """Export results to an HTML file."""
    with open(filename, "w") as f:
        f.write("""
<html>
<head><title>AWS Policy Analyzer Report</title></head>
<body>
<h1>AWS Policy Analyzer Report</h1>
""")
        if results:
            for item in results:
                f.write(f"<h2>Policy: {item['PolicyName']}</h2>\n")
                f.write(f"<p><strong>Policy ARN:</strong> {item['PolicyArn']}</p>\n")
                f.write("<ul>\n")
                for finding in item['Findings']:
                    statement = finding['Statement']
                    action = statement.get('Action', '')
                    resource = statement.get('Resource', '')
                    reason = finding.get('Reason', '')
                    risk = finding.get('Risk', '')
                    f.write(f"<li>Action: <code>{action}</code> | Resource: <code>{resource}</code> | Risk: <strong>{risk}</strong> | Reason: {reason}</li>\n")
                f.write("</ul>\n")
        else:
            f.write("<p>✅ No risky policies found.</p>\n")
        f.write("</body></html>")
    print(f"✅ HTML report saved to: {filename}")


def export_to_csv(results, filename="policy_report.csv"):
    """Export results to a CSV file."""
    with open(filename, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["PolicyName", "PolicyArn", "Action", "Resource", "Risk", "Reason"])
        writer.writeheader()
        if results:
            for item in results:
                for finding in item['Findings']:
                    stmt = finding['Statement']
                    writer.writerow({
                        "PolicyName": item['PolicyName'],
                        "PolicyArn": item['PolicyArn'],
                        "Action": stmt.get('Action', ''),
                        "Resource": stmt.get('Resource', ''),
                        "Risk": finding.get('Risk', ''),
                        "Reason": finding.get('Reason', '')
                    })
        else:
            writer.writerow({
                "PolicyName": "None",
                "PolicyArn": "None",
                "Action": "",
                "Resource": "",
                "Risk": "None",
                "Reason": "No risky policies found."
            })
    print(f"✅ CSV report saved to: {filename}")
    
    

def export_to_excel(results, filename="policy_report.xlsx"):
    """Export results to an Excel (.xlsx) file."""
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["PolicyName", "PolicyArn", "Action", "Resource", "Risk", "Reason"])
    if results:
        for item in results:
            for finding in item['Findings']:
                stmt = finding['Statement']
                sheet.append([
                    item['PolicyName'], 
                    item['PolicyArn'], 
                    stmt.get('Action', ''), 
                    stmt.get('Resource', ''), 
                    finding.get('Risk', ''), 
                    finding.get('Reason', '')
                ])
    else:
        sheet.append(["None", "None", "", "", "None", "No risky policies found."])
    workbook.save(filename)
    print(f"✅ Excel (.xlsx) report saved to: {filename}")



if __name__ == '__main__':
    try:
        results = scan()
        if results:
            print("\n🚩 Risky Policies Found:\n")
            print(json.dumps(results, indent=4))
        else:
            print("\n✅ No risky policies found.")
        # Export results
        export_to_markdown(results, "policy_report.md")
        export_to_html(results, "policy_report.html")
        export_to_csv(results, "policy_report.csv")
        export_to_excel(results, "policy_report.xlsx")
    except botocore.exceptions.NoCredentialsError:
        print("\n❌ No AWS credentials found.")
        print("Please configure your AWS credentials by one of the following methods:\n")
        print("1️⃣ Export environment variables:\n   $env:AWS_ACCESS_KEY_ID='your-access-key'\n   $env:AWS_SECRET_ACCESS_KEY='your-secret'\n   $env:AWS_DEFAULT_REGION='us-east-1'\n")
        print("2️⃣ Or run:\n   aws configure\n\n3️⃣ Or use the offline version:\n   python src/aws_policy_analyzer_mock.py\n")



