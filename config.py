"""
Configuration settings for WhisperNotes App.
"""

import os

# OpenRouter API Configuration
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

# Whisper Model Configuration
WHISPER_MODEL_NAME = "base"  # Options: tiny, base, small, medium, large

# LLM Configuration
LLM_MODEL = "openai/gpt-oss-20b:free"  # Model to use via OpenRouter
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 400

# File Configuration
DEFAULT_OUTPUT_FILE = "transcript.txt"

# UI Configuration
APP_TITLE = "WhisperNotes APP"
APP_DESCRIPTION = "Transcribe speech with Whisper; optionally summarize using any LLM via OpenRouter"
