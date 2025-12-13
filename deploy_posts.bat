@echo off
chcp 65001
echo ==========================================
echo 🚀 Lazy Prompt Content Factory & Deployer
echo ==========================================
echo.

echo 1️⃣  Generating Content from list.xlsx...
python auto_post_factory.py
if %errorlevel% neq 0 (
    echo ❌ Python Script Failed!
    pause
    exit /b %errorlevel%
)

echo.
echo 2️⃣  Deploying to GitHub/Vercel...
git add .
git commit -m "Auto-Deploy: New Content from Factory"
git push origin main

echo.
echo ==========================================
echo ✅ All Done! Your site will update in 1-2 mins.
echo ==========================================
pause
