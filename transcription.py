"""
Transcription functions using OpenAI Whisper.
"""


def transcribe_audio(audio_path, whisper_model):
    """
    Transcribe audio file using Whisper.
    
    Args:
        audio_path (str): Path to audio file
        whisper_model (whisper.Whisper): Loaded Whisper model
    
    Returns:
        str: Transcribed text from audio
        
    Raises:
        FileNotFoundError: If audio file does not exist
        Exception: If transcription fails
    """
    result = whisper_model.transcribe(audio_path)
    return result["text"]
