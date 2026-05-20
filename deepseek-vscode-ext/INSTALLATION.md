# Setup and Installation Guide

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] Visual Studio Code (latest version)
- [ ] Node.js >= 18.x ([Download](https://nodejs.org/))
- [ ] Python >= 3.10 ([Download](https://www.python.org/))
- [ ] pip package manager
- [ ] 8GB+ RAM (16GB+ recommended)
- [ ] 20GB+ free disk space (for model and dependencies)
- [ ] GPU (optional but recommended): NVIDIA with CUDA support

## Step-by-Step Installation

### Step 1: Install Backend Dependencies

```bash
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

**This will install:**
- torch (PyTorch)
- transformers (Hugging Face)
- accelerate
- fastapi
- uvicorn
- bitsandbytes (for GPU optimization)

### Step 2: Install VS Code Extension Dependencies

```bash
cd ../vscode-extension

# Install Node dependencies
npm install

# Build the extension
npm run esbuild
```

### Step 3: Install CLI Dependencies

```bash
cd ../cli

# Install Python packages
pip install -r requirements.txt
```

## Running the Application

### Terminal 1: Start Backend Server

```bash
cd backend

# Activate venv if not already active
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate      # Windows

# Start server
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Wait for message:** `Application startup complete`

### Terminal 2: Test the CLI

```bash
cd cli

# Check server health
python deepseek_cli.py health

# Try a completion
python deepseek_cli.py complete "def fibonacci(n):"

# Try code review
python deepseek_cli.py review <your_file.py>
```

### Terminal 3: Use VS Code Extension

1. Open VS Code
2. Press `Ctrl+Shift+D` or use Command Palette
3. Search for "DeepSeek" commands
4. Use the features!

## Verification Checklist

- [ ] Backend server is running (check http://localhost:8000/health)
- [ ] CLI can connect to server (`python cli/deepseek_cli.py health`)
- [ ] VS Code extension is loaded (check status bar)
- [ ] Model is downloaded (~3GB)
- [ ] No errors in terminal outputs

## Common Installation Issues

### Issue: "pip command not found"
**Solution:** Python is not in PATH. Install Python with "Add to PATH" option.

### Issue: "ModuleNotFoundError: No module named 'torch'"
**Solution:** Make sure virtual environment is activated and run `pip install -r requirements.txt`

### Issue: "Model download fails"
**Solution:** Check internet connection. Model is ~3GB. Delete `.cache/huggingface` and retry.

### Issue: "CUDA not found"
**Solution:** Either install CUDA or set `DEVICE=cpu` in backend/.env (slower)

### Issue: "Port 8000 already in use"
**Solution:** Change PORT in .env or kill process using port 8000

## Next Steps

1. **Read the README.md** for detailed feature documentation
2. **Configure settings** in VS Code (Ctrl+,)
3. **Explore examples** in the docs/
4. **Report issues** on GitHub

## System Requirements by Use Case

### Basic Usage (CPU)
- 8GB RAM
- Python >= 3.10
- Node.js >= 18
- 20GB disk space

### Optimal Usage (GPU)
- 16GB+ RAM
- NVIDIA GPU with 6GB+ VRAM
- CUDA 11.8+
- cuDNN
- 20GB+ disk space

### Professional Usage
- 32GB+ RAM
- High-end NVIDIA GPU (RTX 3090, A6000, etc.)
- Multiple GPUs support
- NVMe SSD

## Getting Help

1. Check terminal output for error messages
2. Run `python -m deepseek_cli.py health`
3. Check server logs at http://localhost:8000/health
4. Review troubleshooting section in README.md

---

**Installation complete! Start using DeepSeek. 🚀**
