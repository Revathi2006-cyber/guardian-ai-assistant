import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import pyttsx3
import os
from rapidfuzz import fuzz  # ✅ NLP fuzzy matching

# Initialize TTS engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def record_audio(filename="output.wav", duration=4, fs=44100):
    """Record user's voice for duration seconds and save as WAV"""
    try:
        print("Listening for emergency... Speak now.")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        wav.write(filename, fs, recording)
    except Exception as e:
        speak(f"Recording failed: {e}")

def listen():
    """Capture and convert speech to text using Google Speech API"""
    filename = "output.wav"
    record_audio(filename)

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Internet issue. Could not reach Google.")
        return ""
    finally:
        if os.path.exists(filename):
            os.remove(filename)

def detect_emergency(command):
    """Use fuzzy matching to detect emergency-related phrases in the voice command"""
    emergency_keywords = [
        "help", "save me", "danger", "i am in danger", "emergency",
        "attack", "kidnap", "fire", "accident", "rape", "call police"
    ]
    for word in emergency_keywords:
        similarity = fuzz.partial_ratio(word, command)
        if similarity >= 80:
            print(f"Matched '{word}' with similarity {similarity}")
            return True
    return False

# 🔧 MAIN function for testing
if __name__ == "__main__":
    speak("Guardian Assistant is ready. Please speak now.")
    user_command = listen()

    if user_command:
        if detect_emergency(user_command):
            speak("Emergency detected. Taking action now.")
        else:
            speak("No emergency detected. You're safe.")
    else:
        speak("No command received.")
