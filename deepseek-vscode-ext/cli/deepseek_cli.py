#!/usr/bin/env python3
"""
Universal AI Model CLI Assistant
Works with any Hugging Face model for code generation and review
"""

import argparse
import requests
import sys
import json
from typing import Optional
from pathlib import Path

class DeepSeekCLI:
    def __init__(self, server_url: str = "http://localhost:8000"):
        self.server_url = server_url
        self.session = requests.Session()

    def check_health(self) -> bool:
        """Check if backend server is running"""
        try:
            response = self.session.get(f"{self.server_url}/health", timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    def get_current_model(self) -> Optional[dict]:
        """Get current model information"""
        try:
            response = self.session.get(f"{self.server_url}/health", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error: {e}", file=sys.stderr)
            return None

    def list_available_models(self) -> Optional[dict]:
        """List available models"""
        try:
            response = self.session.get(f"{self.server_url}/api/models", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error: {e}", file=sys.stderr)
            return None

    def load_model(self, model_name: str) -> Optional[dict]:
        """Load a different model"""
        try:
            response = self.session.post(
                f"{self.server_url}/api/models/load",
                json={"model_name": model_name},
                timeout=300  # Long timeout for model download
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error: {e}", file=sys.stderr)
            return None


    def complete(self, prompt: str, max_tokens: int = 256, temperature: float = 0.7) -> Optional[str]:
        """Generate code completion"""
        try:
            response = self.session.post(
                f"{self.server_url}/api/complete",
                json={
                    "prompt": prompt,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json()["completion"]
        except requests.RequestException as e:
            print(f"Error: {e}", file=sys.stderr)
            return None

    def review(self, code: str, language: str = "python") -> Optional[str]:
        """Review code"""
        try:
            response = self.session.post(
                f"{self.server_url}/api/review",
                json={
                    "code": code,
                    "language": language,
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json()["review"]
        except requests.RequestException as e:
            print(f"Error: {e}", file=sys.stderr)
            return None

    def interactive_mode(self):
        """Start interactive conversation mode"""
        model_info = self.get_current_model()
        if model_info:
            print(f"🚀 AI Model CLI Assistant")
            print(f"📊 Model: {model_info.get('model', 'Unknown')}")
            print(f"🖥️  Device: {model_info.get('device', 'Unknown')}")
            print("📝 Type your code prompt (or 'quit' to exit)\n")
        else:
            print("🚀 AI Model CLI Assistant")
            print("⚠️  Warning: Could not connect to server")
            print("📝 Type your code prompt (or 'quit' to exit)\n")

        conversation_history = ""
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ["quit", "exit", "q"]:
                    print("Goodbye! 👋")
                    break
                
                if not user_input:
                    continue

                conversation_history += f"\n{user_input}"
                
                print("AI: ", end="", flush=True)
                completion = self.complete(conversation_history)
                
                if completion:
                    print(completion)
                    conversation_history += f"\n{completion}"
                else:
                    print("(No response)")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
            except EOFError:
                print("\nGoodbye! 👋")
                break

def main():
    parser = argparse.ArgumentParser(
        description="Universal AI Model CLI Assistant - Works with any Hugging Face model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  deepseek-cli

  # Show current model
  deepseek-cli models

  # Load a different model
  deepseek-cli load "codellama/CodeLlama-7b"

  # Complete a prompt
  deepseek-cli complete "def hello():"

  # Review a file
  deepseek-cli review mycode.py

  # Generate with custom parameters
  deepseek-cli complete "import " --max-tokens 100 --temperature 0.5
        """
    )

    parser.add_argument(
        "--server",
        type=str,
        default="http://localhost:8000",
        help="Backend server URL (default: http://localhost:8000)"
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Generate code completion")
    complete_parser.add_argument("prompt", help="Code prompt")
    complete_parser.add_argument("--max-tokens", type=int, default=256, help="Max tokens to generate")
    complete_parser.add_argument("--temperature", type=float, default=0.7, help="Temperature (0-1)")

    # Review command
    review_parser = subparsers.add_parser("review", help="Review code")
    review_parser.add_argument("file", help="Code file to review")
    review_parser.add_argument("--language", type=str, help="Programming language")

    # Health command
    subparsers.add_parser("health", help="Check server health")

    # Model commands
    models_parser = subparsers.add_parser("models", help="List available models")
    
    load_parser = subparsers.add_parser("load", help="Load a different model")
    load_parser.add_argument("model_name", help="Model name (e.g., gpt2, meta-llama/Llama-2-7b-hf)")
    
    status_parser = subparsers.add_parser("status", help="Show current model status")

    args = parser.parse_args()

    cli = DeepSeekCLI(args.server)

    # Handle commands
    if args.command == "complete":
        if not cli.check_health():
            print("❌ Backend server not running. Start it with: python backend/main.py", file=sys.stderr)
            sys.exit(1)
        
        result = cli.complete(args.prompt, args.max_tokens, args.temperature)
        if result:
            print(result)
        else:
            sys.exit(1)

    elif args.command == "review":
        if not cli.check_health():
            print("❌ Backend server not running. Start it with: python backend/main.py", file=sys.stderr)
            sys.exit(1)
        
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"❌ File not found: {args.file}", file=sys.stderr)
            sys.exit(1)

        code = file_path.read_text()
        language = args.language or file_path.suffix.lstrip(".")
        
        print(f"📋 Reviewing {args.file}...\n")
        result = cli.review(code, language)
        if result:
            print(result)
        else:
            sys.exit(1)

    elif args.command == "health":
        if cli.check_health():
            print("✅ Backend server is healthy")
        else:
            print("❌ Backend server is not responding")
            sys.exit(1)

    elif args.command == "models":
        if not cli.check_health():
            print("❌ Backend server not running. Start it with: python backend/main.py", file=sys.stderr)
            sys.exit(1)
        
        models = cli.list_available_models()
        if models:
            print("\n📊 Available Models:")
            print("=" * 60)
            
            if "current_model" in models:
                print(f"📍 Currently Loaded: {models['current_model']}\n")
            
            if "suggested_models" in models:
                print("✨ Suggested Models:")
                for model in models["suggested_models"]:
                    print(f"  • {model['name']:<40} ({model['size']})")
            
            print("\nUsage: deepseek-cli load \"<model-name>\"")
        else:
            sys.exit(1)

    elif args.command == "load":
        if not cli.check_health():
            print("❌ Backend server not running. Start it with: python backend/main.py", file=sys.stderr)
            sys.exit(1)
        
        print(f"⏳ Loading model: {args.model_name}")
        result = cli.load_model(args.model_name)
        if result:
            print(f"✅ Model loaded successfully!")
            if "status" in result:
                print(f"Status: {result['status']}")
        else:
            print(f"❌ Failed to load model", file=sys.stderr)
            sys.exit(1)

    elif args.command == "status":
        if not cli.check_health():
            print("❌ Backend server not running. Start it with: python backend/main.py", file=sys.stderr)
            sys.exit(1)
        
        model_info = cli.get_current_model()
        if model_info:
            print("\n📊 Model Status:")
            print("=" * 60)
            print(f"Model:  {model_info.get('model', 'Unknown')}")
            print(f"Device: {model_info.get('device', 'Unknown')}")
            print(f"8-Bit:  {'Enabled' if model_info.get('8bit_enabled') else 'Disabled'}")
        else:
            sys.exit(1)

    else:
        # Interactive mode
        if not cli.check_health():
            print("⚠️  Warning: Backend server not running at", args.server)
            print("   Start it with: python backend/main.py\n")
        
        cli.interactive_mode()

if __name__ == "__main__":
    main()
