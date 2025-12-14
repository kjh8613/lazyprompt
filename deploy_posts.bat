@echo off
chcp 65001
echo ==========================================
echo 🚀 Lazy Prompt Content Factory & Deployer
echo ==========================================
echo.

echo 🔑 Please enter your OpenAI API Keys
echo (Press Enter to skip optional keys 2 and 3)
echo.

set /p OPENAI_API_KEY="API Key 1 (Required): "
if "%OPENAI_API_KEY%"=="" (
    echo ❌ ERROR: At least one API key is required!
    pause
    exit /b 1
)

set /p OPENAI_API_KEY_2="API Key 2 (Optional): "
set /p OPENAI_API_KEY_3="API Key 3 (Optional): "

echo.
echo ==========================================
echo 1️⃣  Generating Content from list.xlsx...
echo ==========================================
echo.

python auto_post_factory.py
if %errorlevel% neq 0 (
    echo ❌ Python Script Failed!
    pause
    exit /b %errorlevel%
)

echo.
echo 2️⃣  Deploying to GitHub/Netlify...
git add .
git commit -m "Auto-Deploy: New Content from Factory"
git push origin main

echo.
echo ==========================================
echo ✅ All Done! Your site will update in 1-2 mins.
echo ==========================================
pause
