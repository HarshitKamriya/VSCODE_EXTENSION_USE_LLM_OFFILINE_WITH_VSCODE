@echo off
REM DeepSeek R1 VS Code Integration - Quick Start Script (Windows)

echo.
echo 🚀 DeepSeek R1 VS Code Integration - Quick Start
echo ==================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not installed.
    exit /b 1
)

REM Check Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is required but not installed.
    exit /b 1
)

REM Check npm
npm --version >nul 2>&1
if errorlevel 1 (
    echo ❌ npm is required but not installed.
    exit /b 1
)

echo ✅ All prerequisites found
echo.

REM Installation
echo 📦 Installing dependencies...

REM Backend
echo   Installing backend...
cd backend
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -q -r requirements.txt
cd ..
echo   ✅ Backend ready
echo.

REM Extension
echo   Installing extension...
cd vscode-extension
call npm install -q
call npm run esbuild -q
cd ..
echo   ✅ Extension ready
echo.

REM CLI
echo   Installing CLI...
cd cli
pip install -q -r requirements.txt
cd ..
echo   ✅ CLI ready
echo.

echo 🎉 Installation complete!
echo.
echo 📝 Next steps:
echo.
echo 1️⃣  Start the backend server (open a new command prompt):
echo    cd backend
echo    venv\Scripts\activate
echo    python -m uvicorn main:app --reload
echo.
echo 2️⃣  Load VS Code extension:
echo    - Open VS Code
echo    - Press Ctrl+Shift+D
echo    - Go to Run ^> Run Extension
echo.
echo 3️⃣  Test CLI (open another command prompt):
echo    python cli\deepseek_cli.py health
echo.
echo 4️⃣  Try your first completion:
echo    python cli\deepseek_cli.py complete "def hello():"
echo.
echo 📚 For more information, see:
echo    - README.md       - Full documentation
echo    - EXAMPLES.md     - Usage examples
echo    - INSTALLATION.md - Detailed setup guide
echo.
echo ⚠️  First run will download the model (~3GB). Be patient!
echo.
pause
