"""
Import verification script.
Run this to ensure all modules load correctly before launching the app.
"""

def test_imports():
    """Test that all modules import successfully."""
    print("🔍 Testing imports...\n")
    
    try:
        print("  ✓ Importing config...")
        import config
        
        print("  ✓ Importing models...")
        from models import get_openai_client, load_whisper_model
        
        print("  ✓ Importing transcription...")
        from transcription import transcribe_audio
        
        print("  ✓ Importing summarization...")
        from summarization import summarize_text
        
        print("  ✓ Importing file_ops...")
        from file_ops import save_transcript
        
        print("  ✓ Importing pipeline...")
        from pipeline import process_audio
        
        print("  ✓ Importing ui...")
        from ui import create_gradio_interface, launch_interface
        
        print("\n✅ All imports successful!")
        return True
        
    except Exception as e:
        print(f"\n❌ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_imports()
    exit(0 if success else 1)
