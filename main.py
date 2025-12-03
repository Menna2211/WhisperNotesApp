"""
Main entry point for WhisperNotes App.
"""

from models import get_openai_client, load_whisper_model
from pipeline import process_audio
from ui import create_gradio_interface, launch_interface


def main():
    """
    Initialize and launch the WhisperNotes App.
    
    Loads models and LLM client, creates Gradio interface, and launches the web app.
    """
    print("🔧 Initializing WhisperNotes App...")
    
    # Load models and clients once at startup
    print("📦 Loading Whisper model...")
    whisper_model = load_whisper_model()
    
    print("🔑 Initializing OpenRouter client...")
    llm_client = get_openai_client()
    
    # Define UI handler
    def ui_handler(audio, enable_summary):
        return process_audio(audio, enable_summary, whisper_model, llm_client)
    
    # Create and launch interface
    print("🎨 Creating Gradio interface...")
    interface = create_gradio_interface(ui_handler)
    
    print("🚀 Launching app...")
    launch_interface(interface)


if __name__ == "__main__":
    main()
