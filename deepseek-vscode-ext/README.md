# 🚀 DeepSeek R1 VS Code Integration

A complete offline AI coding assistant powered by DeepSeek R1 1.5B model, featuring VS Code extension, FastAPI backend, and CLI tool.

## 📋 Features

- **VS Code Extension**: Inline code completion and code review directly in VS Code
- **FastAPI Backend**: High-performance inference server for DeepSeek R1 1.5B
- **CLI Tool**: Command-line interface for standalone code assistance
- **Offline Operation**: No internet required, runs entirely on your machine
- **GPU Acceleration**: Supports CUDA for faster inference
- **Code Review**: Automated code review with suggestions

## 🛠️ System Requirements

- **Visual Studio Code** (latest)
- **Node.js** >= 18.x
- **Python** >= 3.10
- **GPU** (Optional but recommended): NVIDIA GPU with CUDA support
- **RAM**: Minimum 8GB (16GB+ recommended)

## 📦 Installation

### 1. Backend Setup

```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Copy environment configuration
cp .env.example .env

# Start the FastAPI server
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

The server will download the DeepSeek model on first run (~3GB).

### 2. VS Code Extension Setup

```bash
cd vscode-extension

# Install dependencies
npm install

# Build extension
npm run esbuild

# (Optional) Watch mode for development
npm run esbuild-watch
```

**Load Extension in VS Code:**
1. Press `Ctrl+Shift+D` (or `Cmd+Shift+D` on Mac)
2. Go to Run and Debug
3. Select "Run Extension"
4. A new VS Code window will open with the extension loaded

Or manually:
1. Open VS Code
2. Press `Ctrl+Shift+X` to open Extensions
3. Click "..." menu → "Install from VSIX"
4. Navigate to `dist/extension.js`

### 3. CLI Tool Setup

```bash
cd cli

# Install Python dependencies
pip install -r requirements.txt

# Make the script executable (Linux/Mac)
chmod +x deepseek_cli.py

# Create alias (Optional)
# Add to ~/.bashrc or ~/.zshrc:
alias deepseek="python /path/to/deepseek_cli.py"
```

## 🚀 Quick Start

### 1. Start the Backend Server

```bash
cd backend
python -m uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`

### 2. Use the VS Code Extension

1. Open a code file in VS Code
2. Press `Ctrl+Shift+D` to trigger completion
3. Or use the command palette (`Ctrl+Shift+P`) and search for "DeepSeek"

**Available Commands:**
- `DeepSeek: Complete Code` (Ctrl+Shift+D)
- `DeepSeek: Review Code`
- `DeepSeek: Start Backend Server`
- `DeepSeek: Configure Settings`

### 3. Use the CLI Assistant

**Interactive Mode:**
```bash
python cli/deepseek_cli.py
# Type your code prompts and get completions
```

**Generate Completion:**
```bash
python cli/deepseek_cli.py complete "def factorial(n):"
```

**Review Code:**
```bash
python cli/deepseek_cli.py review mycode.py
```

**Check Server Health:**
```bash
python cli/deepseek_cli.py health
```

## ⚙️ Configuration

### VS Code Settings

Access settings with `Ctrl+,` and search for "deepseek-copilot":

```json
{
  "deepseek-copilot.serverUrl": "http://localhost:8000",
  "deepseek-copilot.autoComplete": true,
  "deepseek-copilot.temperature": 0.7,
  "deepseek-copilot.maxTokens": 256
}
```

### Backend Configuration

Edit `backend/.env`:

```env
# Device: cuda or cpu
DEVICE=cuda

# Model name
MODEL_NAME=deepseek-ai/deepseek-coder-1.3b-base

# Generation parameters
MAX_LENGTH=2048
TEMPERATURE=0.7
TOP_P=0.95

# Server configuration
HOST=0.0.0.0
PORT=8000
```

## 📊 API Endpoints

### Health Check
```bash
GET /health

Response:
{
  "status": "healthy",
  "model": "deepseek-ai/deepseek-coder-1.3b-base",
  "device": "cuda",
  "model_loaded": true
}
```

### Code Completion
```bash
POST /api/complete

Request:
{
  "prompt": "def hello():",
  "max_tokens": 256,
  "temperature": 0.7,
  "top_p": 0.95
}

Response:
{
  "completion": "    print('Hello, World!')",
  "prompt": "def hello():",
  "model": "deepseek-ai/deepseek-coder-1.3b-base",
  "tokens_used": 45
}
```

### Code Review
```bash
POST /api/review

Request:
{
  "code": "x = 1\ny = 2\nz = x + y",
  "language": "python"
}

Response:
{
  "review": "Code looks clean and simple...",
  "issues": [],
  "suggestions": []
}
```

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
netstat -tuln | grep 8000

# Kill the process using port 8000
lsof -ti:8000 | xargs kill -9
```

### Model download fails
```bash
# Manually download the model
python -c "from transformers import AutoModel; AutoModel.from_pretrained('deepseek-ai/deepseek-coder-1.3b-base')"
```

### Out of Memory (OOM) errors
- Reduce `MAX_LENGTH` in backend/.env
- Use CPU instead of GPU (set `DEVICE=cpu`)
- Close other applications
- Increase system swap space

### Extension can't connect to server
1. Verify server is running: `curl http://localhost:8000/health`
2. Check firewall settings
3. Update `serverUrl` in VS Code settings
4. Check browser console for errors (F12)

## 📚 Project Structure

```
deepseek-vscode-ext/
├── backend/                    # Python FastAPI server
│   ├── main.py                # Main application
│   ├── requirements.txt        # Python dependencies
│   └── .env.example           # Configuration template
├── vscode-extension/          # VS Code extension
│   ├── src/
│   │   └── extension.ts       # Extension code
│   ├── package.json           # Extension manifest
│   ├── tsconfig.json          # TypeScript config
│   └── dist/                  # Compiled extension
├── cli/                       # Command-line interface
│   ├── deepseek_cli.py        # CLI application
│   ├── deepseek_client.py     # API client
│   └── requirements.txt        # Python dependencies
└── README.md                  # This file
```

## 🔧 Development

### Build from Source

```bash
# Backend
cd backend && pip install -r requirements.txt

# Extension
cd vscode-extension && npm install && npm run esbuild

# CLI
cd cli && pip install -r requirements.txt
```

### Running Tests

```bash
# Test backend API
curl -X POST http://localhost:8000/api/complete \
  -H "Content-Type: application/json" \
  -d '{"prompt": "def hello():", "max_tokens": 100}'

# Test CLI
python cli/deepseek_cli.py health
```

## 📈 Performance Tips

1. **Use GPU**: Install CUDA and set `DEVICE=cuda` in .env
2. **Reduce max_tokens**: Smaller values = faster responses
3. **Increase temperature**: Higher values = more creative but slower
4. **Batch requests**: Process multiple completions in sequence

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and create a Pull Request

## 📄 License

MIT License - See LICENSE file for details

## 🔗 Resources

- [DeepSeek Official](https://www.deepseek.com/)
- [Hugging Face Model Card](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [VS Code Extension API](https://code.visualstudio.com/api)

## ⚠️ Important Notes

- **First Run**: Model download (~3GB) may take several minutes
- **GPU Required**: CPU-only inference is very slow for 1.5B model
- **Privacy**: All processing happens locally, no data sent to external servers
- **Offline**: Works completely offline after initial setup

## 📞 Support

For issues and questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review GitHub issues
3. Create a new GitHub issue with detailed information

---

**Happy Coding with DeepSeek! 🚀**
