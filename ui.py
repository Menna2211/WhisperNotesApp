"""
Gradio UI setup and interface creation.
"""

import gradio as gr
from config import APP_TITLE, APP_DESCRIPTION


def create_gradio_interface(process_audio_fn):
    """
    Create and configure Gradio interface for WhisperNotes App.
    
    Args:
        process_audio_fn (callable): Function that handles audio processing.
                                    Signature: fn(audio_path, enable_summary) -> (transcript, summary, file_path)
    
    Returns:
        gr.Interface: Configured Gradio interface
    """
    return gr.Interface(
        fn=process_audio_fn,
        inputs=[
            gr.Audio(type="filepath", label="Record or Upload Audio"),
            gr.Checkbox(label="Summarize Transcript?", value=False),
        ],
        outputs=[
            gr.Textbox(label="Transcript"),
            gr.Textbox(label="Summary"),
            gr.File(label="Download Transcript"),
        ],
        title=APP_TITLE,
        description=APP_DESCRIPTION,
    )


def launch_interface(interface):
    """
    Launch the Gradio interface.
    
    Args:
        interface (gr.Interface): Configured Gradio interface
    """
    interface.launch()
