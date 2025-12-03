"""
File I/O operations for saving transcripts and summaries.
"""

from pathlib import Path
from config import DEFAULT_OUTPUT_FILE


def save_transcript(transcript, summary=None, output_file=None):
    """
    Save transcript (and optionally summary) to a text file.
    
    Args:
        transcript (str): Transcribed text
        summary (str): Optional summary text
        output_file (str): Output file path. Defaults to config value.
    
    Returns:
        str: Path to saved file
        
    Raises:
        IOError: If file cannot be written
    """
    if output_file is None:
        output_file = DEFAULT_OUTPUT_FILE
    
    output_text = transcript
    if summary:
        output_text += "\n\n--- Summary ---\n" + summary
    
    file_path = Path(output_file)
    file_path.write_text(output_text, encoding="utf-8")
    return str(file_path)
