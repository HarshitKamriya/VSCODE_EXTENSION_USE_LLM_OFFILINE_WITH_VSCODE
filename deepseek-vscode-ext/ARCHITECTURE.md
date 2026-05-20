# Architecture Overview

## System Components

```
┌─────────────────────────────────────────────────────────────────┐
│                      Development Environment                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  VS Code    │  │  Command    │  │  Web Browser        │  │
│  │  Extension  │  │  Line CLI   │  │  (Future)           │  │
│  └──────┬───────┘  └──────┬──────┘  └──────┬───────────────┘  │
│         │                 │                 │                   │
│         └─────────────────┼─────────────────┘                   │
│                           │                                      │
│                    HTTP/REST API                                │
│                      Port 8000                                  │
│                           │                                      │
│         ┌─────────────────┴─────────────────┐                   │
│         │                                   │                   │
│  ┌──────▼──────────────────────────────┐   │                   │
│  │   FastAPI Backend Server            │   │                   │
│  ├──────────────────────────────────────┤   │                   │
│  │  • API Routes                        │   │                   │
│  │  • Request Validation                │   │                   │
│  │  • Response Formatting               │   │                   │
│  └──────┬───────────────────────────────┘   │                   │
│         │                                   │                   │
│  ┌──────▼──────────────────────────────┐   │                   │
│  │   Model Inference Engine            │   │                   │
│  ├──────────────────────────────────────┤   │                   │
│  │  • DeepSeek R1 1.5B Model            │   │                   │
│  │  • Token Generation                  │   │                   │
│  │  • GPU Acceleration (CUDA)           │   │                   │
│  └──────┬───────────────────────────────┘   │                   │
│         │                                   │                   │
│  ┌──────▼──────────────────────────────┐   │                   │
│  │   Hardware Layer                    │   │                   │
│  ├──────────────────────────────────────┤   │                   │
│  │  • GPU/CPU                           │   │                   │
│  │  • RAM (8GB+ recommended)            │   │                   │
│  │  • Storage (~20GB for model)         │   │                   │
│  └──────────────────────────────────────┘   │                   │
│                                               │                   │
└────────────────────────────────────────────────┘                   
```

## Component Details

### 1. VS Code Extension (vscode-extension/)
- **Language**: TypeScript
- **Framework**: VS Code API
- **Key Files**:
  - `src/extension.ts` - Main extension logic
  - `package.json` - Manifest and configuration
  - `tsconfig.json` - TypeScript configuration

**Responsibilities**:
- Command registration (complete, review, configure)
- UI/UX (status bar, notifications, progress)
- HTTP requests to backend
- Configuration management
- Error handling and logging

### 2. FastAPI Backend (backend/)
- **Language**: Python
- **Framework**: FastAPI + Uvicorn
- **Key Files**:
  - `main.py` - Application entry point
  - `.env` - Configuration
  - `requirements.txt` - Dependencies

**Responsibilities**:
- API endpoint management
- Request validation (Pydantic models)
- Model loading and inference
- Token generation and management
- Error handling and logging
- CORS handling for cross-origin requests

### 3. CLI Tool (cli/)
- **Language**: Python
- **Type**: Standalone command-line application
- **Key Files**:
  - `deepseek_cli.py` - Main CLI application
  - `deepseek_client.py` - API client wrapper
  - `requirements.txt` - Dependencies

**Responsibilities**:
- Interactive mode for conversations
- Command-line argument parsing
- File I/O operations
- API client communication
- Output formatting

## Data Flow

### Code Completion Flow
```
User Input (Code Prompt)
    ↓
VS Code Extension / CLI
    ↓
HTTP POST /api/complete
    ↓
FastAPI Server
    ↓
Model Inference (DeepSeek R1)
    ↓
Token Generation
    ↓
Response Formatting
    ↓
HTTP Response
    ↓
User Output (Code Completion)
```

### Code Review Flow
```
User Code File
    ↓
VS Code Extension / CLI
    ↓
HTTP POST /api/review
    ↓
FastAPI Server
    ↓
Review Prompt Construction
    ↓
Model Inference
    ↓
Review Generation
    ↓
Response Formatting
    ↓
HTTP Response
    ↓
User Output (Review Report)
```

## API Specification

### Endpoints

#### 1. Health Check
```
GET /health
Response: {
  "status": "healthy",
  "model": "deepseek-ai/deepseek-coder-1.3b-base",
  "device": "cuda|cpu",
  "model_loaded": true|false
}
```

#### 2. Code Completion
```
POST /api/complete
Request: {
  "prompt": "string",
  "max_tokens": 256,
  "temperature": 0.7,
  "top_p": 0.95
}
Response: {
  "completion": "string",
  "prompt": "string",
  "model": "string",
  "tokens_used": int
}
```

#### 3. Code Review
```
POST /api/review
Request: {
  "code": "string",
  "language": "python|javascript|typescript|java|etc"
}
Response: {
  "review": "string",
  "issues": ["issue1", "issue2"],
  "suggestions": ["suggestion1", "suggestion2"]
}
```

## Technology Stack

### Backend
| Component | Technology | Version |
|-----------|-----------|---------|
| Framework | FastAPI | 0.109.0 |
| Server | Uvicorn | 0.27.0 |
| ML Framework | PyTorch | 2.2.0 |
| Model Hub | Hugging Face | Latest |
| Quantization | bitsandbytes | 0.42.0 |

### Extension
| Component | Technology | Version |
|-----------|-----------|---------|
| Language | TypeScript | 5.3.2 |
| API Client | Axios | 1.6.2 |
| Bundler | esbuild | 0.19.8 |
| Linter | ESLint | 8.55.0 |

### CLI
| Component | Technology | Version |
|-----------|-----------|---------|
| Language | Python | 3.10+ |
| HTTP Client | requests | 2.31.0 |
| CLI Framework | argparse | built-in |

## Deployment Options

### 1. Local Development
- Backend runs on localhost:8000
- Extension runs in VS Code
- Best for development and testing

### 2. Docker
```bash
docker-compose up
# Backend available at localhost:8000
```

### 3. Production
- Deploy backend to cloud platform
- Update extension serverUrl setting
- CLI points to remote server

## Performance Characteristics

### Inference Time (Single Completion)
| Device | 1.5B Model | Time |
|--------|-----------|------|
| NVIDIA RTX 3090 | Yes | ~1-2 sec |
| NVIDIA RTX 4080 | Yes | ~0.5-1 sec |
| CPU (i7) | Yes | ~10-30 sec |

### Memory Usage
| Component | RAM | VRAM |
|-----------|-----|------|
| Backend + Model (GPU) | 2GB | 6-8GB |
| Backend + Model (CPU) | 8-12GB | N/A |
| VS Code Extension | 50-100MB | N/A |
| CLI Tool | 50-100MB | N/A |

## Security Architecture

```
┌─────────────────────────────────────────────┐
│  User Machine (Isolated/Offline)            │
├─────────────────────────────────────────────┤
│                                              │
│  ┌─────────────────────────────────────┐   │
│  │ VS Code / CLI                        │   │
│  └────────────┬────────────────────────┘   │
│               │ Localhost Only               │
│  ┌────────────▼────────────────────────┐   │
│  │ FastAPI Backend                      │   │
│  │ (Port 8000 - Default Localhost)     │   │
│  └────────────┬────────────────────────┘   │
│               │                              │
│  ┌────────────▼────────────────────────┐   │
│  │ Model & GPU/CPU                      │   │
│  │ (Local Processing Only)              │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ✅ NO Internet Connection Required         │
│  ✅ NO Data Leaves Machine                  │
│  ✅ COMPLETE Privacy                       │
│  ✅ NO Cloud Dependencies                  │
│                                              │
└──────────────────────────────────────────────┘
```

---

For implementation details, see the source code and developer documentation.
