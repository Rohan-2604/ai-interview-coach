# app.py
import streamlit as st
import random
import os  # Import os to check for API key
from ai_feedback import get_gemini_feedback
from questions import sample_questions
from voice_input import get_voice_input, speak_text

st.set_page_config(page_title="AI Interview Coach", layout="centered", initial_sidebar_state="collapsed")

st.title("🚀 AI Interview Coach")
st.markdown("""
Welcome to your personal AI Interview Coach! Practice common interview questions and get instant, structured feedback powered by Google's Gemini AI.
""")

# Check for API key at startup (moved here for more immediate feedback to user)
# The ai_feedback.py will also check, but this provides a more prominent initial warning.
if not (os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", None)):  # Added None default for st.secrets.get
    st.error("🚨 **API Key Missing!** To run this app, you need a `GEMINI_API_KEY`.")
    st.markdown("1. Get your key from [Google AI Studio](https://aistudio.google.com/).")
    st.markdown(
        "2. **For local use (PyCharm/VS Code):** Set it as a system environment variable named `GEMINI_API_KEY`.")
    st.markdown(
        "3. **For Streamlit Cloud deployment:** Go to your app's settings on Streamlit Cloud and add `GEMINI_API_KEY` as a secret.")
    st.stop()  # Stop the app execution here

# Initialize session state variables
if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(sample_questions)
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = ""
if 'mode' not in st.session_state:
    st.session_state.mode = "text"  # Default to text input

# --- Question Display ---
st.subheader("💡 Current Interview Question:")
st.info(st.session_state.current_question)

# --- Mode Selection (Text vs. Voice) ---
st.markdown("---")  # Separator
st.subheader("Choose Your Input Method:")
col1, col2 = st.columns(2)
with col1:
    if st.button("🎤 Use Voice Input Mode", use_container_width=True, disabled=(st.session_state.mode == "voice")):
        st.session_state.mode = "voice"
        st.session_state.user_answer = ""  # Clear previous answer when switching mode
        st.session_state.feedback = ""  # Clear feedback
        st.rerun()
with col2:
    if st.button("📝 Use Text Input Mode", use_container_width=True, disabled=(st.session_state.mode == "text")):
        st.session_state.mode = "text"
        st.session_state.user_answer = ""  # Clear previous answer when switching mode
        st.session_state.feedback = ""  # Clear feedback
        st.rerun()

st.markdown("---")  # Separator

# --- User Input Area ---
current_text_input = ""  # Placeholder for the current value in the text_area
submitted_via_text = False  # Flag to indicate if text submit button was pressed

if st.session_state.mode == "text":
    st.write("### Type your answer below:")
    current_text_input = st.text_area(
        "Your Answer:",
        value=st.session_state.user_answer,  # Display what's in session_state (e.g., after a submit)
        height=250,
        placeholder="Type your detailed answer here... (e.g., using STAR method for behavioral questions)",
        key="text_input_area"
    )
    # Check if the text submit button was pressed
    submitted_via_text = st.button("🚀 Get Feedback (Text Input)", type="primary", use_container_width=True,
                                   disabled=(not current_text_input.strip()))
else:  # Voice Input Mode
    st.write("### Record your answer:")
    st.write("*(Ensure your microphone is connected and allowed by your browser/OS)*")
    record_button = st.button("🎙️ Start Recording", type="primary", use_container_width=True)

    # Placeholder for displaying transcribed text
    transcribed_text_display = st.empty()

    if record_button:
        print("DEBUG (Terminal): 'Start Recording' button was clicked and its block is executing!")  # NEW DEBUG PRINT
        # Clear previous recording info
        st.session_state.user_answer = ""
        st.session_state.feedback = ""
        transcribed_text_display.empty()  # Clear previous transcribed text area

        spoken_text = get_voice_input()  # This function will handle internal feedback via st.sidebar
        if spoken_text:
            st.session_state.user_answer = spoken_text
            transcribed_text_display.text_area("Your Transcribed Answer:", value=spoken_text, height=100, disabled=True)
        # No else needed, get_voice_input handles its own errors/warnings in sidebar

    # Determine if voice submit button should be enabled based on whether voice input was successfully transcribed
    submitted_via_voice = st.button(
        "🚀 Get Feedback (Voice Input)",
        type="primary",
        use_container_width=True,
        disabled=(not st.session_state.user_answer.strip())
    )
    # For voice mode, st.session_state.user_answer is already updated by get_voice_input
    # The submission check below will use st.session_state.user_answer directly.

# --- Handle submission based on mode ---
# This block handles saving the input and triggering feedback.
# It runs *before* the main feedback display.
if st.session_state.mode == "text" and submitted_via_text:
    st.session_state.user_answer = current_text_input  # Save the text input to session state
    # This will trigger a rerun. On the next rerun, the condition below will be true.
    st.rerun()  # Rerun to process the newly saved user_answer
elif st.session_state.mode == "voice" and submitted_via_voice:
    # For voice, st.session_state.user_answer is already set by get_voice_input
    # We just need to rerun to process it.
    st.rerun()

# --- Feedback Generation and Display ---
# This block now relies solely on st.session_state.user_answer being correctly set.
# The 'submitted_via_text' and 'submitted_via_voice' are handled above with st.rerun().
# So, this block essentially runs on the rerun *after* a submission.

# Only attempt to generate feedback if st.session_state.user_answer is NOT empty
# AND we don't already have feedback (to avoid re-generating on every rerun).
if st.session_state.user_answer.strip() and not st.session_state.feedback:
    print("DEBUG (Terminal): Entering feedback generation block because user_answer is set.")  # Confirmation print
    print(f"DEBUG (Terminal): Processing answer: '{st.session_state.user_answer}'")
    with st.spinner("Analyzing your answer with Gemini AI... This might take a few moments."):
        feedback = get_gemini_feedback(st.session_state.user_answer, st.session_state.current_question)
        st.session_state.feedback = feedback  # Store whatever feedback (or error message) is returned
        st.markdown("---")
        st.subheader("📊 Feedback from AI Coach:")

        if st.session_state.feedback.strip():  # Check if feedback is not empty or just whitespace
            st.markdown(st.session_state.feedback)  # Use markdown to render bullet points from LLM
        else:
            st.warning(
                "No feedback content received from the AI. Please check the terminal for errors or try a different answer.")

        # Optional: TTS for feedback
        st.markdown("---")
        if st.button("🔊 Read Feedback Aloud", use_container_width=True):
            with st.spinner("Reading aloud..."):
                speak_text(st.session_state.feedback)
            st.success("Feedback read aloud!")

# Display feedback if it exists (even on subsequent reruns after generation)
elif st.session_state.feedback.strip():
    st.markdown("---")
    st.subheader("📊 Feedback from AI Coach:")
    st.markdown(st.session_state.feedback)
    st.markdown("---")
    if st.button("🔊 Read Feedback Aloud", use_container_width=True):
        with st.spinner("Reading aloud..."):
            speak_text(st.session_state.feedback)
        st.success("Feedback read aloud!")

# --- New Question Button ---
st.markdown("---")
if st.button("➡️ Next Question", use_container_width=True):
    st.session_state.current_question = random.choice(sample_questions)
    st.session_state.feedback = ""  # Clear previous feedback
    st.session_state.user_answer = ""  # Clear previous answer
    st.session_state.mode = "text"  # Reset mode for new question by default
    st.rerun()

st.markdown("---")
st.caption("Built with Streamlit and Google Gemini API.")