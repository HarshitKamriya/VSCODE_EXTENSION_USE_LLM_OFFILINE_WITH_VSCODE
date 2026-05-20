# 🎯 Quick Reference - Common Commands

## Installation Commands

```bash
# Install everything
make install-all

# Or manually:
cd backend && pip install -r requirements.txt
cd ../vscode-extension && npm install
cd ../cli && pip install -r requirements.txt
```

---

## Running the Application

### Backend Server
```bash
# Start with auto-reload
cd backend
python -m uvicorn main:app --reload

# Or with Makefile
make backend-run
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

### VS Code Extension
```bash
# Build extension
cd vscode-extension
npm run esbuild

# Watch for changes
npm run esbuild-watch

# Load in VS Code
# Press F5 or Ctrl+Shift+D
```

### CLI Tool
```bash
# Interactive mode
python cli/deepseek_cli.py

# Check health
python cli/deepseek_cli.py health

# Complete code
python cli/deepseek_cli.py complete "def hello():"

# Review code
python cli/deepseek_cli.py review myfile.py
```

---

## Testing

```bash
# Test backend API
curl http://localhost:8000/health

# Test CLI
python cli/deepseek_cli.py health

# Test completion
python cli/deepseek_cli.py complete "import "
```

---

## Development Commands (Using Makefile)

```bash
# Installation
make install              # Install all dependencies
make install-backend      # Install backend only
make install-extension    # Install extension only
make install-cli          # Install CLI only

# Running
make backend-run          # Start backend server
make extension-build      # Build extension
make extension-watch      # Watch for extension changes
make cli-test             # Test CLI

# Utilities
make clean                # Clean build artifacts
make verify-installation  # Verify setup
make docs                 # Open documentation
make help                 # Show all commands
```

---

## Docker Commands

```bash
# Build and run
docker-compose up

# Run in background
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f deepseek-backend

# Rebuild
docker-compose down && docker-compose up --build
```

---

## VS Code Commands

### Keyboard Shortcuts
| Action | Shortcut |
|--------|----------|
| Code Completion | Ctrl+Shift+D (Cmd+Shift+D on Mac) |
| Command Palette | Ctrl+Shift+P |
| Open Settings | Ctrl+, |
| Debug/Run Extension | F5 |
| Toggle Terminal | Ctrl+` |

### Command Palette Commands
```
DeepSeek: Complete Code
DeepSeek: Review Code
DeepSeek: Start Backend Server
DeepSeek: Stop Backend Server
DeepSeek: Configure Settings
```

---

## Configuration Quick Reference

### Backend (.env)
```env
DEVICE=cuda                    # Use GPU
DEVICE=cpu                     # Use CPU
TEMPERATURE=0.7                # Balance
TEMPERATURE=0.5                # Conservative
MAX_LENGTH=2048                # Full context
```

### VS Code Settings
```json
{
  "deepseek-copilot.serverUrl": "http://localhost:8000",
  "deepseek-copilot.temperature": 0.7,
  "deepseek-copilot.maxTokens": 256
}
```

### CLI Arguments
```bash
# Temperature
python cli/deepseek_cli.py complete "prompt" --temperature 0.5

# Max tokens
python cli/deepseek_cli.py complete "prompt" --max-tokens 100

# Server
python cli/deepseek_cli.py --server http://192.168.1.100:8000 health
```

---

## Troubleshooting Commands

```bash
# Check Python version
python --version

# Check Node.js version
node --version

# Check if port 8000 is available
netstat -tuln | grep 8000    # Linux/Mac
netstat -ano | findstr :8000 # Windows

# Kill process on port 8000
lsof -ti:8000 | xargs kill -9    # Linux/Mac
taskkill /PID <PID> /F           # Windows

# Check if backend is running
curl http://localhost:8000/health

# View backend logs
# Check terminal where uvicorn is running

# Check extension logs
# VS Code → View → Output → Extension Host
```

---

## File Locations

```
Project Root:
c:\Users\hp\OneDrive\Documents\New project\deepseek-vscode-ext\

Backend:
c:\Users\hp\OneDrive\Documents\New project\deepseek-vscode-ext\backend\

Extension:
c:\Users\hp\OneDrive\Documents\New project\deepseek-vscode-ext\vscode-extension\

CLI:
c:\Users\hp\OneDrive\Documents\New project\deepseek-vscode-ext\cli\

Documentation:
README.md, QUICKSTART.md, INSTALLATION.md, etc.
```

---

## API Quick Reference

### Health Check
```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "model": "deepseek-ai/deepseek-coder-1.3b-base",
  "device": "cuda",
  "model_loaded": true
}
```

### Code Completion
```bash
curl -X POST http://localhost:8000/api/complete \
  -H "Content-Type: application/json" \
  -d '{"prompt": "def hello():", "max_tokens": 100}'
```

### Code Review
```bash
curl -X POST http://localhost:8000/api/review \
  -H "Content-Type: application/json" \
  -d '{"code": "x = 1", "language": "python"}'
```

---

## Environment Variables

```bash
# Python cache
export PYTHONPATH=/path/to/backend

# Hugging Face cache
export HF_HOME=/custom/path

# CUDA device
export CUDA_VISIBLE_DEVICES=0

# Disable telemetry
export HF_HUB_DISABLE_TELEMETRY=1
```

---

## Performance Tuning Quick Settings

### For Maximum Speed
```env
DEVICE=cuda
TEMPERATURE=0.5
MAX_LENGTH=256
```

### For Better Quality
```env
DEVICE=cuda
TEMPERATURE=0.7
MAX_LENGTH=2048
```

### For Limited Resources
```env
DEVICE=cpu
TEMPERATURE=0.7
MAX_LENGTH=512
```

---

## First Time Setup

```bash
# 1. Navigate to project
cd deepseek-vscode-ext

# 2. Install dependencies
make install

# 3. Terminal 1: Start backend
make backend-run

# 4. Terminal 2: Test CLI
make cli-test

# 5. VS Code: Open project and press Ctrl+Shift+D
```

---

## Daily Workflow

```bash
# Terminal 1: Backend
cd backend
python -m uvicorn main:app --reload

# Terminal 2: Watch extension (optional)
cd vscode-extension
npm run esbuild-watch

# Terminal 3: Test/use CLI
python cli/deepseek_cli.py
```

---

## Cleanup

```bash
# Remove build artifacts
make clean

# Remove virtual environment (be careful!)
rm -rf backend/venv

# Remove node_modules
rm -rf vscode-extension/node_modules

# Remove Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
```

---

## Emergency Commands

```bash
# Kill hanging process
kill -9 $(lsof -ti:8000)  # Linux/Mac

# Force restart
docker-compose down && docker-compose up

# Reset everything
make clean && make install-all
```

---

## Documentation Quick Links

```
QUICKSTART.md      → 5-minute setup
README.md          → Full documentation
INSTALLATION.md    → Detailed setup
EXAMPLES.md        → Usage examples
CONFIG.md          → Configuration
ARCHITECTURE.md    → System design
```

---

## Useful Tips

💡 **Tip 1**: Use `make help` to see all Makefile commands
💡 **Tip 2**: Check docs before troubleshooting
💡 **Tip 3**: Use `curl` to test API directly
💡 **Tip 4**: Watch extension changes with `npm run esbuild-watch`
💡 **Tip 5**: Check health endpoint to verify setup

---

## One-Liner Commands

```bash
# Install and test
make install && make cli-test

# Full setup
make install && make backend-run &

# Quick test
curl http://localhost:8000/health && python cli/deepseek_cli.py health

# Clean and reinstall
make clean && make install-all
```

---

## Environment Presets

### Development Environment
```bash
DEVICE=cuda
TEMPERATURE=0.7
MAX_LENGTH=2048
DEBUG=true
```

### Production Environment
```bash
DEVICE=cuda
TEMPERATURE=0.5
MAX_LENGTH=1024
DEBUG=false
HOST=0.0.0.0
PORT=8000
```

### Testing Environment
```bash
DEVICE=cpu
TEMPERATURE=0.7
MAX_LENGTH=512
DEBUG=true
```

---

**Save this file for quick reference!**

*For detailed information, see the main documentation files.*
