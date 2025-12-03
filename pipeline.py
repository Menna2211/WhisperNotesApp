"""
Pipeline orchestration: coordinates transcription, summarization, and file saving.
"""

from transcription import transcribe_audio
from summarization import summarize_text
from file_ops import save_transcript


def process_audio(audio_path, enable_summary, whisper_model, llm_client):
    """
    Complete pipeline: transcribe → optionally summarize → save to file.
    
    Args:
        audio_path (str): Path to audio file
        enable_summary (bool): Whether to generate a summary
        whisper_model (whisper.Whisper): Loaded Whisper model
        llm_client (OpenAI): OpenAI client configured for OpenRouter
    
    Returns:
        tuple: (transcript, summary, file_path)
            - transcript (str): Full transcribed text
            - summary (str): Summary text (empty string if not enabled)
            - file_path (str): Path to saved transcript file
    """
    # Step 1: Transcribe audio
    transcript = transcribe_audio(audio_path, whisper_model)
    
    # Step 2: Summarize if requested
    summary = ""
    if enable_summary:
        summary = summarize_text(transcript, llm_client)
    
    # Step 3: Save to file
    file_path = save_transcript(transcript, summary if enable_summary else None)
    
    return transcript, summary, file_path
