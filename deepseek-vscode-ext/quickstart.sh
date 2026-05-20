#!/bin/bash

# DeepSeek R1 VS Code Integration - Quick Start Script
# This script sets up and runs the entire application

set -e

echo "🚀 DeepSeek R1 VS Code Integration - Quick Start"
echo "=================================================="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo "📋 Checking prerequisites..."

command -v python3 >/dev/null 2>&1 || { echo -e "${RED}Python 3 is required but not installed.${NC}"; exit 1; }
command -v node >/dev/null 2>&1 || { echo -e "${RED}Node.js is required but not installed.${NC}"; exit 1; }
command -v npm >/dev/null 2>&1 || { echo -e "${RED}npm is required but not installed.${NC}"; exit 1; }

echo -e "${GREEN}✅ All prerequisites found${NC}"
echo ""

# Installation
echo "📦 Installing dependencies..."

# Backend
echo "  Installing backend..."
cd backend
python3 -m venv venv 2>/dev/null || true
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null || true
pip install -q -r requirements.txt
cd ..
echo -e "  ${GREEN}✅ Backend ready${NC}"

# Extension
echo "  Installing extension..."
cd vscode-extension
npm install -q
npm run esbuild -q 2>/dev/null || echo "Note: Extension requires npm build"
cd ..
echo -e "  ${GREEN}✅ Extension ready${NC}"

# CLI
echo "  Installing CLI..."
cd cli
pip install -q -r requirements.txt
cd ..
echo -e "  ${GREEN}✅ CLI ready${NC}"

echo ""
echo -e "${GREEN}🎉 Installation complete!${NC}"
echo ""

# Instructions
echo "📝 Next steps:"
echo ""
echo "1️⃣  Start the backend server (run in one terminal):"
echo "   cd backend"
echo "   source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
echo "   python -m uvicorn main:app --reload"
echo ""
echo "2️⃣  Load VS Code extension:"
echo "   - Open VS Code"
echo "   - Press Ctrl+Shift+D (or Cmd+Shift+D on Mac)"
echo "   - Go to Run → Run Extension"
echo ""
echo "3️⃣  Test CLI (in another terminal):"
echo "   python cli/deepseek_cli.py health"
echo ""
echo "4️⃣  Try your first completion:"
echo "   python cli/deepseek_cli.py complete \"def hello():\""
echo ""
echo "📚 For more information, see:"
echo "   - README.md       - Full documentation"
echo "   - EXAMPLES.md     - Usage examples"
echo "   - INSTALLATION.md - Detailed setup guide"
echo ""
echo -e "${YELLOW}⚠️  First run will download the model (~3GB). Be patient!${NC}"
echo ""
