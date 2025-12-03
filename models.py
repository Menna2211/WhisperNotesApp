"""
Model initialization functions for Whisper and OpenAI clients.
"""

import whisper
from openai import OpenAI
from config import OPENROUTER_BASE_URL, OPENROUTER_API_KEY, WHISPER_MODEL_NAME


def get_openai_client():
    """
    Initialize and return OpenRouter client with API key from config.
    
    Returns:
        OpenAI: Configured OpenAI client pointing to OpenRouter API
    """
    return OpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=OPENROUTER_API_KEY,
    )


def load_whisper_model(model_name=None):
    """
    Load and return Whisper model.
    
    Args:
        model_name: Model size (tiny, base, small, medium, large).
                   Defaults to config value.
    
    Returns:
        whisper.Whisper: Loaded Whisper model
    """
    if model_name is None:
        model_name = WHISPER_MODEL_NAME
    return whisper.load_model(model_name)
