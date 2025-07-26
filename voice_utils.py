import os
import io
import uuid
import soundfile as sf
import sounddevice as sd
import streamlit as st
import speech_recognition as sr
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),  # required
)

def record_audio_google_stt():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 बोलिए...")
        audio = recognizer.listen(source, phrase_time_limit=6)

    try:
        st.info("📝 ट्रांसक्राइब किया जा रहा है...")
        return recognizer.recognize_google(audio, language="hi-IN")
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return ""

def synthesize_speech(text):
    
    voice_id = os.getenv("ELEVENLABS_VOICE_ID", "Kalpana")  # fallback voice

    # Generate audio using correct method from ElevenLabs client
    audio_stream = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
        text=text,
    )

    path = f"output_{uuid.uuid4()}.mp3"
    with open(path, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    return path