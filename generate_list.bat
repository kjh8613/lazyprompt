@echo off
chcp 65001
echo ==========================================
echo 🎨 Lazy Prompt - List Generator
echo ==========================================
echo Generate niche, Western-focused blog topics!
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
echo 🚀 Starting List Generator...
echo ==========================================
echo.

python list_generator.py

echo.
pause
