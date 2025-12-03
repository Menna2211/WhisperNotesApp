# WhisperNotes App 🎤

A modular, production-ready transcription and summarization application that combines **OpenAI's Whisper** (speech-to-text) with **LLM summarization** (via OpenRouter) in an easy-to-use **Gradio web interface**.

---

## 🎯 Features

- **🎙️ Speech-to-Text Transcription** — Convert audio files to text using Whisper
- **✨ Optional AI Summarization** — Summarize transcripts using any LLM via OpenRouter
- **💾 Auto-Save** — Export transcripts and summaries to `.txt` files
- **🌐 Web Interface** — User-friendly Gradio UI (no command line needed)
- **📦 Modular Code** — Clean separation of concerns; easy to test and extend

---

## 📋 System Requirements

- **Python 3.8+**
- **FFmpeg** (required by Whisper for audio processing)
  - **Windows**: [Download](https://ffmpeg.org/download.html) or `choco install ffmpeg`
  - **macOS**: `brew install ffmpeg`
  - **Linux**: `sudo apt-get install ffmpeg`

---

## 🚀 Installation

### 1. Clone or Navigate to Project
```powershell
git clone https://github.com/Menna2211/WhisperNotesApp.git
```

### 2. Create Virtual Environment (Optional but Recommended)
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

---

## 🔑 Configuration

### API Key Setup

The app uses **OpenRouter** to access various LLMs. You need an API key:

1. **Get your API key**: Sign up at [openrouter.ai](https://openrouter.ai) and copy your API key
2. **Set environment variable**:
   ```powershell
   $env:OPENROUTER_API_KEY = "your-api-key-here"
   ```
   Or add to your `.env` file (if using `python-dotenv`)

3. **Or update `config.py`** (not recommended for production):
   ```python
   OPENROUTER_API_KEY = "your-api-key-here"
   ```

### Model Selection

Edit `config.py` to customize:

```python
# Whisper model size (tiny, base, small, medium, large)
WHISPER_MODEL_NAME = "base"

# LLM model via OpenRouter (free and paid options available)
LLM_MODEL = "openai/gpt-oss-20b:free"

# LLM parameters
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 400
```

---

## 💻 Usage

### Quick Start
```powershell
python main.py
```

The app will:
1. Load Whisper and LLM models (~2-5 seconds)
2. Launch a Gradio web server (usually `http://localhost:7860`)
3. Open in your default browser

### Using the App

1. **Record or Upload Audio**
   - Click "Record or Upload Audio"
   - Either record live or upload an `.mp3`, `.wav`, `.m4a`, etc.

2. **Optional: Enable Summarization**
   - Check "Summarize Transcript?" if you want an AI summary

3. **Submit**
   - Click the submit button
   - Wait for transcription (~10-30s depending on audio length and model)

4. **Results**
   - View transcript in the "Transcript" box
   - View summary in the "Summary" box (if enabled)
   - Download as `.txt` file

---

## 📁 Project Structure

```
WhisperNotesApp/
├── main.py              # Entry point; orchestrates initialization and launch
├── config.py            # Settings (API keys, model names, UI text)
├── models.py            # Initialize Whisper and OpenAI clients
├── transcription.py     # Audio → text via Whisper
├── summarization.py     # Text → summary via LLM
├── file_ops.py          # Save transcripts to files
├── pipeline.py          # Orchestrates transcription → summarization → save
├── ui.py                # Gradio interface setup
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

### File Responsibilities

| File | Purpose |
|------|---------|
| `config.py` | Single source of truth for settings |
| `models.py` | Model & client initialization |
| `transcription.py` | Whisper transcription logic |
| `summarization.py` | LLM summarization logic |
| `file_ops.py` | File I/O and transcript saving |
| `pipeline.py` | Coordinates the full workflow |
| `ui.py` | Gradio UI creation and launching |
| `main.py` | Entry point; ties everything together |

---

## 🔧 Advanced Usage

### Use in Python Scripts

```python
from models import get_openai_client, load_whisper_model
from pipeline import process_audio

# Initialize
whisper_model = load_whisper_model()
llm_client = get_openai_client()

# Process an audio file
transcript, summary, file_path = process_audio(
    audio_path="path/to/audio.mp3",
    enable_summary=True,
    whisper_model=whisper_model,
    llm_client=llm_client
)

print(f"Transcript: {transcript}")
print(f"Summary: {summary}")
print(f"Saved to: {file_path}")
```

### Transcription Only (No Summarization)

```python
from models import load_whisper_model
from transcription import transcribe_audio

whisper_model = load_whisper_model()
transcript = transcribe_audio("audio.mp3", whisper_model)
print(transcript)
```

### Custom Summarization Parameters

```python
from summarization import summarize_text

summary = summarize_text(
    text="Your long text here...",
    client=llm_client,
    model="openai/gpt-4-turbo",  # Different model
    temperature=0.5,              # More deterministic
    max_tokens=200                # Shorter summary
)
```

---

## 📊 Supported Audio Formats

Whisper supports most common formats:
- `.mp3`, `.wav`, `.m4a`, `.flac`, `.ogg`, `.wma`, `.aac`, and more

---

## ⚙️ Performance Tips

1. **Faster Transcription**: Use a smaller Whisper model
   ```python
   # In config.py
   WHISPER_MODEL_NAME = "tiny"  # Fastest, lower accuracy
   WHISPER_MODEL_NAME = "base"  # Good balance (default)
   WHISPER_MODEL_NAME = "small" # Better accuracy, slower
   ```

2. **Lower API Costs**: Use free LLM models
   ```python
   LLM_MODEL = "openai/gpt-oss-20b:free"  # Free tier
   LLM_MODEL = "google/gemini-2.0-flash-lite"  # Alternative free option
   ```

3. **Batch Processing**: Use `process_audio()` in a loop for multiple files

---

## 🐛 Troubleshooting

### Issue: "FFmpeg not found"
**Solution**: Install FFmpeg
```powershell
# Windows with Chocolatey
choco install ffmpeg

# Or download from https://ffmpeg.org/download.html
```

### Issue: "OPENROUTER_API_KEY not found"
**Solution**: Set environment variable
```powershell
$env:OPENROUTER_API_KEY = "sk-or-v1-..."
```

### Issue: "CUDA out of memory" (GPU error)
**Solution**: Use a smaller Whisper model in `config.py`
```python
WHISPER_MODEL_NAME = "tiny"  # Much faster
```

### Issue: API rate limit exceeded
**Solution**: Wait a few moments or reduce `LLM_MAX_TOKENS` in `config.py`

---

## 📚 Examples

### Example 1: Transcribe a Meeting
```powershell
python main.py
# → Upload meeting_recording.mp3
# → Check "Summarize Transcript?"
# → Get transcript and summary
```

### Example 2: Batch Process Multiple Files
```python
import os
from models import get_openai_client, load_whisper_model
from pipeline import process_audio

whisper_model = load_whisper_model()
llm_client = get_openai_client()

audio_files = ["file1.mp3", "file2.mp3", "file3.mp3"]

for audio_file in audio_files:
    transcript, summary, file_path = process_audio(
        audio_path=audio_file,
        enable_summary=True,
        whisper_model=whisper_model,
        llm_client=llm_client
    )
    print(f"✅ Processed: {audio_file}")
```

### Example 3: Different Summarization Models
```python
# In config.py or at runtime:
LLM_MODEL = "openai/gpt-4-turbo"           # Best quality, costs $
LLM_MODEL = "google/gemini-2.0-flash"     # Fast, free tier available
LLM_MODEL = "meta-llama/llama-2-70b"      # Open source via OpenRouter
```

---

## 🧪 Testing

### Test Transcription
```python
from models import load_whisper_model
from transcription import transcribe_audio

model = load_whisper_model()
result = transcribe_audio("test_audio.mp3", model)
assert isinstance(result, str)
assert len(result) > 0
print("✅ Transcription works!")
```

### Test Summarization
```python
from models import get_openai_client
from summarization import summarize_text

client = get_openai_client()
test_text = "The quick brown fox jumps over the lazy dog." * 50
summary = summarize_text(test_text, client)
assert isinstance(summary, str)
print("✅ Summarization works!")
```

---

## 📦 Dependencies

See `requirements.txt`:
- `openai` — OpenAI/OpenRouter API client
- `gradio` — Web UI framework
- `openai-whisper` — Speech-to-text model
- `ffmpeg-python` (optional, for local FFmpeg management)

---

## 📝 License

Licensed under the MIT License. See `LICENSE` file for details.

---

## 🤝 Contributing

Found a bug or have a feature request? Feel free to:
1. Open an issue
2. Submit a pull request
3. Contact the maintainers

---

## 💡 Future Enhancements

- [ ] Multi-language support detection
- [ ] Batch processing from UI
- [ ] Custom prompt templates for summarization
- [ ] Save/load conversation history
- [ ] Support for more LLM providers (Anthropic, Hugging Face, etc.)
- [ ] Docker containerization
- [ ] Unit and integration tests

---

## 📞 Support

- **Documentation**: See sections above
- **API Docs**: [OpenRouter](https://openrouter.ai/docs) | [Whisper](https://github.com/openai/whisper)
- **Gradio**: [Gradio Docs](https://www.gradio.app/)

---
