import os
import sounddevice as sd
from scipy.io.wavfile import write
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SAMPLE_RATE = 16000
DURATION = 5  # seconds
AUDIO_FILE = "input.wav"


def record_audio():
    print("🎤 Listening... Speak now")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    write(AUDIO_FILE, SAMPLE_RATE, audio)
    print("✅ Recording complete")


def speech_to_text() -> str:
    record_audio()

    with open(AUDIO_FILE, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
            response_format="text"
        )

    return transcription
