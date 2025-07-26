# voice_input.py
import speech_recognition as sr
import pyttsx3
import streamlit as st
import time


def get_voice_input():
    """
    Captures voice input from the microphone and converts it to text.
    Returns the recognized text or None if an error occurs.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.sidebar.info("👂 Listening... Please speak clearly into your microphone.")
        # Calibrate for ambient noise levels
        r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
        try:
            r.adjust_for_ambient_noise(source, duration=1)
            # Listen for audio with a timeout
            audio = r.listen(source, timeout=8, phrase_time_limit=8)  # Max 8 seconds of phrase
        except sr.WaitTimeoutError:
            st.sidebar.warning("⏳ No speech detected within the timeout period. Please try again.")
            return None
        except Exception as e:
            st.sidebar.error(f"🚫 Error capturing audio: {e}. Check your microphone and system permissions.")
            return None

    try:
        st.sidebar.info("🧠 Processing speech...")
        text = r.recognize_google(audio)
        st.sidebar.success(f"🎤 You said: \"{text}\"")
        return text
    except sr.UnknownValueError:
        st.sidebar.warning("🤔 Speech Recognition could not understand audio. Please speak more clearly or try again.")
        return None
    except sr.RequestError as e:
        st.sidebar.error(
            f"🌐 Could not request results from Google Speech Recognition service; {e}. Check your internet connection.")
        return None
    finally:
        # Clear sidebar info after processing
        st.sidebar.empty()


def speak_text(text):
    """
    Converts text to speech using pyttsx3.
    """
    try:
        engine = pyttsx3.init()
        # Optional: Customize voice, speed, volume
        # You can list available voices with:
        # voices = engine.getProperty('voices')
        # for voice in voices:
        #     print(voice.id, voice.name)
        # Example to set a female voice (index might vary)
        # engine.setProperty('voice', voices[1].id)

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        st.error(
            f"🔊 Error in Text-to-Speech: {e}. On Linux, you might need to install 'espeak-ng' and 'libespeak1'. On Windows, ensure your audio drivers are up to date.")