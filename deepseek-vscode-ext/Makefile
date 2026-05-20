# DeepSeek R1 1.5B VS Code Integration - Makefile
# Quick start commands for all tasks

.PHONY: help install install-backend install-extension install-cli \
        backend-run extension-build extension-watch cli-test \
        clean verify-installation docs

help:
	@echo "DeepSeek R1 VS Code Integration - Available Commands"
	@echo ""
	@echo "Installation:"
	@echo "  make install              - Install all dependencies"
	@echo "  make install-backend      - Install backend dependencies"
	@echo "  make install-extension    - Install extension dependencies"
	@echo "  make install-cli          - Install CLI dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make backend-run          - Start backend server"
	@echo "  make extension-build      - Build VS Code extension"
	@echo "  make extension-watch      - Watch and rebuild extension"
	@echo "  make cli-test             - Test CLI tool"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean                - Remove build artifacts"
	@echo "  make verify-installation  - Verify all components"
	@echo "  make docs                 - Open documentation"
	@echo "  make help                 - Show this help message"

install: install-backend install-extension install-cli
	@echo "✅ All dependencies installed successfully!"

install-backend:
	@echo "📦 Installing backend dependencies..."
	cd backend && pip install -r requirements.txt
	@echo "✅ Backend dependencies installed"

install-extension:
	@echo "📦 Installing extension dependencies..."
	cd vscode-extension && npm install
	cd vscode-extension && npm run esbuild
	@echo "✅ Extension dependencies installed and built"

install-cli:
	@echo "📦 Installing CLI dependencies..."
	cd cli && pip install -r requirements.txt
	@echo "✅ CLI dependencies installed"

backend-run:
	@echo "🚀 Starting DeepSeek backend server..."
	@echo "📍 Server will be available at http://localhost:8000"
	@echo "💡 Tip: In another terminal, run 'make extension-watch' or 'make cli-test'"
	cd backend && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

extension-build:
	@echo "🔨 Building VS Code extension..."
	cd vscode-extension && npm run esbuild
	@echo "✅ Extension built successfully"

extension-watch:
	@echo "👀 Watching for extension changes..."
	cd vscode-extension && npm run esbuild-watch

cli-test:
	@echo "🧪 Testing CLI tool..."
	python cli/deepseek_cli.py health

clean:
	@echo "🧹 Cleaning up build artifacts..."
	cd vscode-extension && rm -rf dist node_modules
	cd backend && rm -rf __pycache__ *.egg-info
	cd cli && rm -rf __pycache__ *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "✅ Clean complete"

verify-installation:
	@echo "🔍 Verifying installation..."
	@echo ""
	@echo "Checking Python..."
	python --version
	@echo ""
	@echo "Checking pip..."
	pip --version
	@echo ""
	@echo "Checking Node.js..."
	node --version
	@echo ""
	@echo "Checking npm..."
	npm --version
	@echo ""
	@echo "Checking backend dependencies..."
	-pip list | grep -E "torch|fastapi|transformers"
	@echo ""
	@echo "Checking CLI health..."
	-python cli/deepseek_cli.py health || echo "⚠️  Backend not running (this is normal if you haven't started it)"
	@echo ""
	@echo "✅ Verification complete"

docs:
	@echo "📚 Opening documentation..."
	@echo "Available docs:"
	@echo "  - README.md          - Main documentation"
	@echo "  - INSTALLATION.md    - Installation guide"
	@echo "  - EXAMPLES.md        - Usage examples"
	@echo ""
	@if command -v xdg-open > /dev/null; then \
		xdg-open README.md; \
	elif command -v open > /dev/null; then \
		open README.md; \
	else \
		echo "Please open README.md manually"; \
	fi

# Development shortcut - run backend and watch extension simultaneously
dev:
	@echo "🚀 Starting development environment..."
	@echo "Run in separate terminals:"
	@echo "  Terminal 1: make backend-run"
	@echo "  Terminal 2: make extension-watch"
	@echo "  Terminal 3: make cli-test"

.DEFAULT_GOAL := help
