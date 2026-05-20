# 🚀 START HERE - DeepSeek R1 VS Code Integration

Welcome! This guide will get you up and running in 5 minutes.

---

## ⚡ Quick Start (5 minutes)

### Step 1: Check Prerequisites
```bash
python --version      # Should be 3.10+
node --version       # Should be 18+
npm --version        # Should exist
```

### Step 2: Install Dependencies
```bash
# Windows
quickstart.bat

# Linux/Mac
bash quickstart.sh

# Or manual
make install-all
```

### Step 3: Start Backend Server
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

**Wait for:** `Application startup complete`

### Step 4: Load Extension in VS Code
1. Open VS Code
2. Press `Ctrl+Shift+D` (or `Cmd+Shift+D` on Mac)
3. Go to Run → "Run Extension"
4. A new VS Code window opens with the extension

### Step 5: Test It Works
```bash
# In a new terminal
python cli/deepseek_cli.py health

# Should show: ✅ Backend server is healthy
```

---

## 📖 Next Steps

### Beginner
1. Read [README.md](README.md) for overview
2. Try examples in [EXAMPLES.md](EXAMPLES.md)
3. Follow [INSTALLATION.md](INSTALLATION.md) for detailed setup

### Intermediate
1. Review [CONFIG.md](CONFIG.md) for settings
2. Check [ARCHITECTURE.md](ARCHITECTURE.md) for system design
3. Explore the code in `backend/`, `vscode-extension/`, `cli/`

### Advanced
1. Read [SECURITY.md](SECURITY.md)
2. See [CONTRIBUTING.md](CONTRIBUTING.md) for development
3. Review [CHANGELOG.md](CHANGELOG.md) for version info

---

## 🎯 Common Tasks

### Use Code Completion in VS Code
1. Open a code file
2. Type some code
3. Press `Ctrl+Shift+D` to get AI suggestions
4. Accept or modify the suggestion

### Review Your Code
1. Open a file
2. Use Command Palette: `Ctrl+Shift+P`
3. Search "DeepSeek: Review Code"
4. See suggestions in output panel

### Interactive CLI Mode
```bash
python cli/deepseek_cli.py
# Type prompts and get responses
```

### Complete Code from CLI
```bash
python cli/deepseek_cli.py complete "def fibonacci(n):"
```

### Review File from CLI
```bash
python cli/deepseek_cli.py review mycode.py
```

---

## 🔧 Troubleshooting

### "Model not found" error
- **Solution**: Model downloads on first run (~3GB). Be patient.
- Ensure 20GB+ free disk space
- Check internet connection

### "Cannot connect to server"
- **Solution**: Make sure backend is running
- Check: `curl http://localhost:8000/health`
- Verify port 8000 is not blocked

### "Out of memory"
- **Solution**: Reduce model size or use CPU
- Edit `.env`: Set `DEVICE=cpu` or reduce `MAX_LENGTH`
- Close other applications

### Slow responses
- **Solution**: Use GPU instead of CPU (see INSTALLATION.md)
- Check: `curl http://localhost:8000/health`
- Reduce `maxTokens` in VS Code settings

### Extension won't load
- **Solution**: Rebuild extension
- Run: `cd vscode-extension && npm install && npm run esbuild`
- Restart VS Code

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| [README.md](README.md) | Complete feature guide |
| [INSTALLATION.md](INSTALLATION.md) | Detailed setup |
| [EXAMPLES.md](EXAMPLES.md) | Usage examples |
| [CONFIG.md](CONFIG.md) | Configuration options |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System design |
| [SECURITY.md](SECURITY.md) | Security info |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [BUILD_SUMMARY.md](BUILD_SUMMARY.md) | What was built |

---

## 💡 Tips

✨ **Press Ctrl+Shift+D** for instant code completion
📖 **Read EXAMPLES.md** for real usage scenarios
⚙️ **Check CONFIG.md** to customize settings
🚀 **Use Makefile** for quick commands
🐛 **Check logs** if something breaks

---

## 🎓 Learning Path

```
START HERE ↓
  ├→ Quick Start (above) ✓
  ├→ README.md (overview)
  ├→ EXAMPLES.md (try features)
  ├→ CONFIG.md (customize)
  ├→ ARCHITECTURE.md (understand)
  └→ Source code (explore)
```

---

## ✅ Verification Checklist

After setup, verify:
- [ ] `python --version` shows 3.10+
- [ ] `node --version` shows 18+
- [ ] Dependencies installed without errors
- [ ] Backend starts and shows "Application startup complete"
- [ ] `python cli/deepseek_cli.py health` shows ✅
- [ ] VS Code extension loads (check status bar)
- [ ] Ctrl+Shift+D works in editor

---

## 🆘 Still Having Issues?

1. **Check logs**: Look at terminal output
2. **Review docs**: Each doc has troubleshooting section
3. **Try examples**: EXAMPLES.md has many scenarios
4. **Check settings**: CONFIG.md explains all options
5. **Read architecture**: ARCHITECTURE.md explains how it works

---

## 🎉 You're All Set!

Everything is installed and ready. Now:

1. **For VS Code**: Open a code file and press Ctrl+Shift+D
2. **For CLI**: Run `python cli/deepseek_cli.py`
3. **For Backend**: Access API at `http://localhost:8000`

---

## 📞 Need Help?

- 📖 **Documentation**: See files listed above
- 🔍 **Troubleshooting**: Each doc has a troubleshooting section
- 💬 **Examples**: Check EXAMPLES.md for real scenarios
- 🏗️ **Architecture**: Read ARCHITECTURE.md for system design

---

## 🚀 Quick Commands

```bash
# Install everything
make install-all

# Start backend (in one terminal)
make backend-run

# Test CLI (in another terminal)
make cli-test

# Watch extension (in third terminal)
cd vscode-extension && npm run esbuild-watch

# Check health
python cli/deepseek_cli.py health

# Build everything
make install && make backend-run
```

---

**Ready to code with AI? Start with pressing Ctrl+Shift+D in VS Code! 🎉**

---

**Questions?** Check the relevant documentation file listed above.

**First time here?** Follow the 5-minute quick start at the top.

**Want to learn more?** Read [README.md](README.md).

---

*Version 0.1.0 | Last Updated: January 2024*
