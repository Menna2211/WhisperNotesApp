"""
Summarization functions using LLM via OpenRouter.
"""

from config import LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS


def summarize_text(text, client, model=None, temperature=None, max_tokens=None):
    """
    Summarize text using LLM via OpenRouter.
    
    Args:
        text (str): Text to summarize
        client (OpenAI): OpenAI client configured for OpenRouter
        model (str): Model to use. Defaults to config value.
        temperature (float): Model temperature. Defaults to config value.
        max_tokens (int): Max tokens for summary. Defaults to config value.
    
    Returns:
        str: Summarized text
        
    Raises:
        Exception: If LLM API call fails
    """
    if model is None:
        model = LLM_MODEL
    if temperature is None:
        temperature = LLM_TEMPERATURE
    if max_tokens is None:
        max_tokens = LLM_MAX_TOKENS
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Please summarize the following text:\n{text}"},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content
