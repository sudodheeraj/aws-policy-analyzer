@echo off
REM ==========================
REM AWS Policy Analyzer Runner
REM ==========================
echo.
echo 🔍 AWS Policy Analyzer
echo.

REM Set your AWS credentials here
set AWS_ACCESS_KEY_ID=your-access-key
set AWS_SECRET_ACCESS_KEY=your-secret-access-key
set AWS_DEFAULT_REGION=us-east-1

echo ✅ AWS environment variables set.
echo.

REM Try to run the online version
echo ⚡️ Running online version...
python src/aws_policy_analyzer.py

if %errorlevel% NEQ 0 (
    echo ❌ AWS online version failed. Running offline mock version...
    python src/aws_policy_analyzer_mock.py
)

echo.
echo 🎉 Done! Results saved as:
echo - policy_report.md
echo - policy_report.html
echo - policy_report.csv
echo - policy_report.xlsx
pause
