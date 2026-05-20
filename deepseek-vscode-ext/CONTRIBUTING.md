# Contributing to DeepSeek R1 VS Code Integration

Thank you for your interest in contributing! We welcome all contributions including bug reports, feature requests, and code improvements.

## Getting Started

### 1. Fork and Clone
```bash
git clone https://github.com/yourusername/deepseek-vscode-ext.git
cd deepseek-vscode-ext
```

### 2. Set Up Development Environment
```bash
# Install all dependencies
make install-all

# Or manually:
cd backend && pip install -r requirements.txt
cd ../vscode-extension && npm install
cd ../cli && pip install -r requirements.txt
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## Development Workflow

### Backend Development

```bash
cd backend

# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run with auto-reload
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest tests/
```

### Extension Development

```bash
cd vscode-extension

# Install dependencies
npm install

# Build
npm run esbuild

# Watch for changes
npm run esbuild-watch

# Lint
npm run lint

# Test in VS Code
# Press F5 or Ctrl+Shift+D to open debug instance
```

### CLI Development

```bash
cd cli

# Test commands
python deepseek_cli.py health
python deepseek_cli.py complete "test"
python deepseek_cli.py review test.py
```

## Code Style

### Python (Backend/CLI)
- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use docstrings for functions

```python
def my_function(param: str) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param: Description of the parameter
        
    Returns:
        Description of the return value
    """
    return True
```

### TypeScript (Extension)
- Use ESLint configuration provided
- Use strict mode
- Add comments for complex logic
- Use meaningful variable names

```typescript
/**
 * Brief description of the function.
 * @param input - Description of input
 * @returns Description of return value
 */
function processInput(input: string): boolean {
  return true;
}
```

### Commit Messages
- Use clear, descriptive messages
- Reference issues: `Fix #123`
- Use imperative mood: "Add feature" not "Added feature"

Examples:
```
Add code completion API endpoint
Fix memory leak in model loading
Update documentation for configuration
Refactor CLI argument parsing
```

## Testing

### Running Tests

```bash
# Backend tests
cd backend
pytest tests/

# Extension tests
cd ../vscode-extension
npm test

# CLI tests
cd ../cli
pytest tests/
```

### Writing Tests

**Python (pytest)**
```python
def test_completion_endpoint():
    """Test code completion endpoint"""
    response = client.post("/api/complete", json={
        "prompt": "def hello():",
        "max_tokens": 50
    })
    assert response.status_code == 200
    assert "completion" in response.json()
```

**TypeScript (Jest)**
```typescript
test('should handle completion request', async () => {
  const result = await client.complete('def hello():');
  expect(result).toBeTruthy();
});
```

## Documentation

### Guidelines
- Keep documentation up-to-date with code changes
- Use clear, concise language
- Include examples for new features
- Update README.md, CONFIG.md, and EXAMPLES.md

### Documentation Files
- **README.md** - Main documentation
- **INSTALLATION.md** - Setup guide
- **EXAMPLES.md** - Usage examples
- **CONFIG.md** - Configuration reference
- **ARCHITECTURE.md** - System design
- **API.md** - API documentation

## Submitting Changes

### 1. Make Your Changes
```bash
# Edit files
# Test thoroughly
# Ensure tests pass
```

### 2. Commit and Push
```bash
git add .
git commit -m "Clear commit message"
git push origin feature/your-feature-name
```

### 3. Create Pull Request
- Use descriptive title
- Reference related issues
- Include what changed and why
- Add tests for new features

**PR Template:**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tested locally
- [ ] Added tests
- [ ] All tests pass

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Pull Request Review

- Be respectful and constructive
- Respond to all comments
- Make requested changes
- Request re-review after changes

## Issues and Bug Reports

### Reporting Bugs

**Template:**
```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [Windows/Linux/Mac]
- Python: [3.10/3.11/3.12]
- Node.js: [18.x/20.x]
- GPU: [Yes/No, which model?]

## Logs
Include relevant error messages

## Additional Context
Any other information
```

### Requesting Features

**Template:**
```markdown
## Feature Request

## Description
What would you like to add?

## Use Case
Why is this needed?

## Proposed Solution
How should it work?

## Alternative Solutions
Other approaches you've considered

## Additional Context
Screenshots, examples, etc.
```

## Project Structure

```
deepseek-vscode-ext/
├── backend/                    # Python FastAPI server
│   ├── main.py
│   ├── requirements.txt
│   └── tests/
├── vscode-extension/           # VS Code extension
│   ├── src/
│   ├── package.json
│   └── tsconfig.json
├── cli/                        # Command-line interface
│   ├── deepseek_cli.py
│   └── deepseek_client.py
├── docs/                       # Documentation
└── README.md
```

## Resources

- [VS Code Extension API](https://code.visualstudio.com/api)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)

## Community

- GitHub Issues: For bug reports and feature requests
- GitHub Discussions: For questions and ideas
- Email: For security issues (security@deepseek.com)

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Given credit in documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to DeepSeek! 🙏**

Questions? Open an issue or discussion on GitHub.
