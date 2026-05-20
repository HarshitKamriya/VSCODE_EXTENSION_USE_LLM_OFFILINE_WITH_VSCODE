# Examples and Usage Scenarios

## Code Completion Examples

### Python Function Completion
```python
# In VS Code, press Ctrl+Shift+D after typing:
def calculate_factorial(n):

# DeepSeek will suggest:
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)
```

### JavaScript React Component
```javascript
// Type this and press Ctrl+Shift+D:
function Button({ onClick, children }) {

// Get suggestions for completing the component
```

### TypeScript Type Definition
```typescript
// Type and complete:
interface User {
    id: number;
    name: string;
    
// Get suggestions for additional properties
```

## Code Review Examples

### Review Python File
```bash
python cli/deepseek_cli.py review mycode.py
```

**Input:**
```python
def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result
```

**DeepSeek Review:**
```
Issues found:
1. Function doesn't validate input
2. No error handling for non-numeric values
3. No docstring

Suggestions:
1. Add type hints
2. Add input validation
3. Consider using list comprehension
4. Add unit tests
```

## Interactive CLI Examples

### Example 1: Web Server Setup
```bash
$ python cli/deepseek_cli.py

You: I need to create a FastAPI server with a hello endpoint

DeepSeek: Here's a basic FastAPI server...

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Run with: uvicorn main:app --reload
```

### Example 2: Data Processing
```bash
You: How do I read a CSV file and filter rows?

DeepSeek: Here's a solution using pandas:

import pandas as pd

df = pd.read_csv('data.csv')
filtered_df = df[df['age'] > 30]
```

### Example 3: Error Debugging
```bash
You: I'm getting a TypeError in my list operation

DeepSeek: This usually happens when types don't match. 
Here are common solutions:

# Check if values are the right type
items = [int(x) for x in items]

# Or use error handling:
try:
    result = [x + 1 for x in items]
except TypeError:
    print("Items must be numbers")
```

## Integration Patterns

### Pattern 1: Inline Code Completion
1. Write partial code in VS Code
2. Press `Ctrl+Shift+D`
3. Review suggestion
4. Accept or modify as needed

### Pattern 2: Code Review Workflow
1. Write code in VS Code
2. Save file
3. Right-click → "DeepSeek: Review Code"
4. Check review in output panel
5. Make improvements based on suggestions

### Pattern 3: CLI-Based Development
```bash
# Start session
python cli/deepseek_cli.py

# Describe what you want to build
You: Create a function to validate email addresses

# Get the code
DeepSeek: [provides email validation code]

# Ask follow-up questions
You: How do I test this function?

DeepSeek: [provides testing code]
```

## Real-World Use Cases

### 1. Learning New Languages
```bash
python cli/deepseek_cli.py complete "Go hello world program:"
# Helps you learn Go syntax quickly
```

### 2. Refactoring Existing Code
- Copy problematic code
- Ask for improvements
- Review suggestions
- Apply changes incrementally

### 3. Documentation Generation
```bash
python cli/deepseek_cli.py complete "# Document this function\ndef complex_logic():"
# Get helpful docstrings and comments
```

### 4. Code Quality Improvement
```bash
python cli/deepseek_cli.py review legacy_code.py
# Get specific suggestions for improvement
```

### 5. Quick Prototyping
- Describe what you need in CLI
- Get working code
- Integrate into your project
- Refine as needed

## Performance Tips

### For Faster Responses
1. Use shorter prompts
2. Lower `max_tokens` value
3. Ensure GPU is used (check backend logs)
4. Close other applications

### For Better Quality
1. Use longer, more descriptive prompts
2. Provide more context
3. Use `temperature: 0.5` for precise code
4. Use `temperature: 0.9` for creative suggestions

## Troubleshooting Examples

### Issue: Slow responses
```bash
# Check if GPU is being used
python backend/main.py  # Look for "cuda" or "cpu" in logs

# If CPU, switch to GPU (see configuration)
```

### Issue: Out of memory
```bash
# Reduce max tokens
python cli/deepseek_cli.py complete "prompt" --max-tokens 100
```

### Issue: Poor quality suggestions
```bash
# Provide more context in prompt
# Instead of: "def func():"
# Try: "def process_json_data(data_string): # Parse JSON and return dict"
```

## Advanced Usage

### Custom Prompt Engineering
```bash
# Good prompt structure:
# 1. Context
# 2. What you want
# 3. Format specification

python cli/deepseek_cli.py complete \
"Python function to validate phone numbers. 
Should accept E.164 format. 
Return True if valid, False otherwise:

def validate_phone_number(phone: str) -> bool:"
```

### Batch Processing
```python
# Use the Python client for batch operations
from deepseek_client import DeepSeekClient

client = DeepSeekClient()

files = ['file1.py', 'file2.py', 'file3.py']
for file in files:
    with open(file) as f:
        code = f.read()
    review = client.review(code)
    print(f"Review for {file}:\n{review}")
```

---

**More examples and tutorials coming soon!**
