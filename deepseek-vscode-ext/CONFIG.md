# Configuration Reference

## Backend Configuration (.env)

```env
# Device Selection
DEVICE=cuda                              # cuda or cpu

# Model Configuration
MODEL_NAME=deepseek-ai/deepseek-coder-1.3b-base
MAX_LENGTH=2048                          # Maximum total token length

# Generation Parameters
TEMPERATURE=0.7                          # 0.0-1.0, higher = more creative
TOP_P=0.95                               # 0.0-1.0, nucleus sampling

# Server Configuration
HOST=0.0.0.0                             # 0.0.0.0 = all interfaces, 127.0.0.1 = localhost only
PORT=8000                                # Server port
```

### Parameter Explanations

#### DEVICE
- **cuda**: Use NVIDIA GPU (recommended for speed)
- **cpu**: Use CPU only (much slower but works on any machine)

#### TEMPERATURE
Controls randomness in output:
- **0.0**: Deterministic, always same output
- **0.5**: Balanced, good for code
- **0.7**: Default, mix of creativity and consistency
- **1.0**: Maximum randomness

#### TOP_P
Nucleus sampling parameter:
- **0.9**: More conservative, follows most probable tokens
- **0.95**: Balanced approach (default)
- **1.0**: No filtering, all tokens considered

#### MAX_LENGTH
Maximum tokens to process:
- **512**: Fast but limited context
- **2048**: Balanced (default)
- **4096**: More context but slower

### Recommended Configurations

#### For Quality Code Completions
```env
DEVICE=cuda
TEMPERATURE=0.5
TOP_P=0.95
MAX_LENGTH=2048
```

#### For Creative Suggestions
```env
DEVICE=cuda
TEMPERATURE=0.8
TOP_P=0.99
MAX_LENGTH=2048
```

#### For CPU-Only (Slow)
```env
DEVICE=cpu
TEMPERATURE=0.7
TOP_P=0.95
MAX_LENGTH=1024
```

#### For Memory-Limited Systems
```env
DEVICE=cuda
TEMPERATURE=0.7
TOP_P=0.9
MAX_LENGTH=512
```

---

## VS Code Extension Settings

Access with: `Ctrl+,` then search "deepseek-copilot"

```json
{
  // Server Configuration
  "deepseek-copilot.serverUrl": "http://localhost:8000",
  
  // Feature Toggles
  "deepseek-copilot.autoComplete": true,
  
  // Generation Parameters
  "deepseek-copilot.temperature": 0.7,      // 0.0-1.0
  "deepseek-copilot.maxTokens": 256         // 1-2048
}
```

### Setting Details

#### serverUrl
The URL of your DeepSeek backend server.

**Examples:**
```json
"deepseek-copilot.serverUrl": "http://localhost:8000"     // Local
"deepseek-copilot.serverUrl": "http://192.168.1.100:8000" // Network
"deepseek-copilot.serverUrl": "https://api.example.com"   // Remote
```

#### autoComplete
Enable/disable inline auto-completion suggestions.

```json
"deepseek-copilot.autoComplete": true    // Enable
"deepseek-copilot.autoComplete": false   // Disable
```

#### temperature
Controls creativity of completions (0-1).

```json
"deepseek-copilot.temperature": 0.5    // Conservative
"deepseek-copilot.temperature": 0.7    // Balanced (default)
"deepseek-copilot.temperature": 0.9    // Creative
```

#### maxTokens
Maximum tokens to generate (1-2048).

```json
"deepseek-copilot.maxTokens": 128      // Fast, shorter completions
"deepseek-copilot.maxTokens": 256      // Balanced (default)
"deepseek-copilot.maxTokens": 512      // More context, slower
```

---

## CLI Tool Configuration

### Command Line Arguments

```bash
# Start interactive mode
python deepseek_cli.py

# Specify server URL
python deepseek_cli.py --server http://192.168.1.100:8000

# Code completion
python deepseek_cli.py complete "prompt" \
  --max-tokens 256 \
  --temperature 0.7

# Code review
python deepseek_cli.py review myfile.py --language python

# Health check
python deepseek_cli.py health
```

### Environment Variables (Future)

```bash
# Set default server
export DEEPSEEK_SERVER=http://localhost:8000

# Set default language
export DEEPSEEK_LANGUAGE=python
```

---

## Docker Configuration

### docker-compose.yml

```yaml
services:
  deepseek-backend:
    # ... container configuration ...
    environment:
      - DEVICE=cpu              # Use CPU in Docker (GPU requires special config)
      - MODEL_NAME=deepseek-ai/deepseek-coder-1.3b-base
      - MAX_LENGTH=2048
      - TEMPERATURE=0.7
      - TOP_P=0.95
    ports:
      - "8000:8000"            # Port mapping
    volumes:
      - model-cache:/root/.cache/huggingface  # Persistent model cache
```

### Running with Docker

```bash
# Build and run
docker-compose up

# Run in background
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f deepseek-backend
```

---

## Performance Tuning

### For Maximum Speed
```env
DEVICE=cuda
TEMPERATURE=0.5
TOP_P=0.9
MAX_LENGTH=256
```
```json
"deepseek-copilot.maxTokens": 128
```

### For Maximum Quality
```env
DEVICE=cuda
TEMPERATURE=0.7
TOP_P=0.95
MAX_LENGTH=2048
```
```json
"deepseek-copilot.maxTokens": 512
```

### For Limited Memory
```env
DEVICE=cpu
TEMPERATURE=0.7
TOP_P=0.9
MAX_LENGTH=512
```
```json
"deepseek-copilot.maxTokens": 128
```

### For Batch Processing
```env
DEVICE=cuda
TEMPERATURE=0.5
TOP_P=0.95
MAX_LENGTH=1024
```

---

## Troubleshooting Configuration Issues

### Issue: Slow Responses
**Solution:**
```env
# Reduce complexity
TEMPERATURE=0.5
MAX_LENGTH=512
```

### Issue: Out of Memory
**Solution:**
```env
# Use CPU fallback and reduce context
DEVICE=cpu
MAX_LENGTH=256
```

### Issue: Cannot Connect
**Solution:**
```json
{
  "deepseek-copilot.serverUrl": "http://127.0.0.1:8000"
}
```

### Issue: Poor Quality Responses
**Solution:**
```env
# Increase temperature and context
TEMPERATURE=0.8
MAX_LENGTH=2048
TOP_P=0.95
```

---

## System Environment Variables

```bash
# Set Python path
export PYTHONPATH=/path/to/backend

# Set cache location
export HF_HOME=/custom/huggingface/path

# Set PyTorch device
export CUDA_VISIBLE_DEVICES=0

# Disable analytics
export HF_HUB_DISABLE_TELEMETRY=1
```

---

For more information, see:
- README.md - Full documentation
- ARCHITECTURE.md - System design
- EXAMPLES.md - Usage examples
