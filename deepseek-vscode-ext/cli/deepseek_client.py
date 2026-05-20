#!/usr/bin/env python3
import requests
from typing import Optional

class DeepSeekClient:
    """Simple wrapper for DeepSeek API"""
    
    def __init__(self, server_url: str = "http://localhost:8000"):
        self.server_url = server_url
        self.base_url = f"{server_url}/api"

    def complete(self, prompt: str, **kwargs) -> str:
        """Generate code completion"""
        response = requests.post(
            f"{self.base_url}/complete",
            json={"prompt": prompt, **kwargs}
        )
        response.raise_for_status()
        return response.json()["completion"]

    def review(self, code: str, language: str = "python") -> str:
        """Review code"""
        response = requests.post(
            f"{self.base_url}/review",
            json={"code": code, "language": language}
        )
        response.raise_for_status()
        return response.json()["review"]
