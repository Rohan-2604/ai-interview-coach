# ai_feedback.py
import os
import google.generativeai as genai
import streamlit as st  # Import Streamlit to use st.error, st.secrets, etc.
import pkg_resources  # Import pkg_resources to check package version

# --- DEBUG: Print installed google-generativeai version ---
try:
    installed_gemini_version = pkg_resources.get_distribution("google-generativeai").version
    st.info(f"DEBUG: google-generativeai version detected: {installed_gemini_version}")
    print(f"DEBUG (Terminal): google-generativeai version detected: {installed_gemini_version}")
except pkg_resources.DistributionNotFound:
    st.error("DEBUG: google-generativeai package not found by pkg_resources in this environment.")
    print("DEBUG (Terminal): google-generativeai package not found by pkg_resources in this environment.")
except Exception as e:
    st.error(f"DEBUG: Error getting google-generativeai version: {e}")
    print(f"DEBUG (Terminal): Error getting google-generativeai version: {e}")
# --------------------------------------------------------


# Configure the Gemini API with your key
api_key = None  # Initialize api_key to None

try:
    # First, try to get the key from Streamlit secrets (for Streamlit Cloud deployment)
    # Wrap in a try-except to handle cases where secrets.toml doesn't exist locally
    st.info("Attempting to retrieve API key from Streamlit secrets...")
    try:
        api_key = st.secrets.get("GEMINI_API_KEY", None)  # Added default None to avoid KeyError if key not in secrets
        if api_key:
            st.info("API key found in Streamlit secrets.")
        else:
            st.warning("API key NOT found in Streamlit secrets (key missing or empty).")
    except Exception as e:
        # Catch any exception related to st.secrets.get() (e.g., FileNotFoundError if .streamlit/secrets.toml is missing)
        st.warning(
            f"An error occurred while checking Streamlit secrets (likely secrets.toml not found locally): {e}. Falling back to environment variables.")

    # If not found in secrets (or an error occurred), try to get it from environment variables
    if not api_key:
        st.info("Attempting to retrieve API key from environment variables...")
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            st.info("API key found in environment variables.")
        else:
            st.error("API key NOT found in environment variables either.")

    # If after both attempts, API key is still not found, stop the app
    if not api_key:
        st.error("🚨 GEMINI_API_KEY not found! Please set it up correctly.")
        st.markdown("For **local development**: Set `GEMINI_API_KEY` as a system/user environment variable.")
        st.markdown("For **Streamlit Cloud deployment**: Add `GEMINI_API_KEY` to your app's secrets.")
        st.stop()  # Stop the Streamlit app execution if API key is missing

    # If API key is found, proceed with configuration
    st.info("Configuring Gemini API...")
    genai.configure(api_key=api_key)
    st.success("Gemini API configured successfully!")

    # --- DEBUG: List available models (Keeping this here for now, good info) ---
    print("\n--- DEBUG: Listing available Gemini models and their supported methods ---")
    st.info("DEBUG: Listing available Gemini models...")
    found_gemini_pro_candidate = False
    try:
        for m in genai.list_models():
            if "generateContent" in m.supported_generation_methods:
                model_info = f"Model: {m.name}, Supported methods: {m.supported_generation_methods}"
                print(f"  {model_info}")
                # We can update this check to look for flash models too if needed for debug message
                if "gemini-1.5-pro" in m.name or "gemini-2.5-pro" in m.name or "gemini-1.5-flash" in m.name:
                    found_gemini_pro_candidate = True
                    st.success(f"DEBUG: Found {m.name} with generateContent support!")
    except Exception as e:
        print(f"  Error listing models: {e}")
        st.error(f"DEBUG: Error listing models: {e}")

    if not found_gemini_pro_candidate:
        st.warning(
            "DEBUG: No suitable 'gemini-pro' or 'gemini-1.5-flash' candidate model found with 'generateContent' support for this API key.")
        print(
            "DEBUG (Terminal): No suitable 'gemini-pro' or 'gemini-1.5-flash' candidate model found with 'generateContent' support for this API key.")
    print("--- DEBUG: End of model list ---")
    # ----------------------------------------

except Exception as e:
    # This outer try-except catches any remaining unexpected errors during the entire configuration block
    st.error(f"❌ An unexpected critical error occurred during API key configuration: {e}.")
    st.markdown("Please double-check your API key validity and system setup.")
    st.stop()


def get_gemini_feedback(user_input, question_asked):
    """
    Sends the user's answer to the Gemini Pro model and gets structured feedback.
    """
    try:
        # CHANGED: Model name to 'models/gemini-1.5-flash'
        model = genai.GenerativeModel('models/gemini-1.5-flash')

        prompt = f"""
        You are an AI interview coach. Your goal is to provide constructive and actionable feedback on interview answers.

        The question asked was: "{question_asked}"
        The user's answer was: "{user_input}"

        Evaluate the user's answer based on the following criteria:
        - **Communication Clarity:** Is the answer easy to understand? Is the language precise and free of jargon (unless appropriate for the context)?
        - **Answer Structure:** Is the answer well-organized (e.g., using STAR method for behavioral questions)? Does it have a clear beginning, middle, and end, making it easy to follow?
        - **Professional Tone:** Is the tone appropriate for a professional interview? Is it confident, respectful, and enthusiastic without being overly casual or arrogant?
        - **Completeness/Relevance:** Does the answer fully address all parts of the question? Is it relevant to the question asked, avoiding unnecessary tangents?
        - **Technical Coverage (optional):** If the question explicitly or implicitly asks for technical details (e.g., "Explain polymorphism in Python" or "Describe a technical challenge"), does the answer demonstrate sufficient and accurate technical understanding? State "Not applicable" if the question is not technical.

        Provide feedback in a structured format with clear bullet points for each criterion.
        After the bullet points, provide one specific, actionable suggestion for improvement that the user can apply to their next answer.

        Example Feedback Format:
        **Feedback for "{question_asked}"**
        - **Communication Clarity:** The answer was mostly clear, but there were a few vague phrases.
        - **Answer Structure:** The structure was a bit disjointed; a more clear introduction and conclusion would help.
        - **Professional Tone:** The tone was generally professional, but could use a bit more enthusiasm.
        - **Completeness/Relevance:** The answer covered the main points, but missed one key aspect of the question.
        - **Technical Coverage:** The technical explanation was accurate but lacked depth in one area.

        **Suggestion for Improvement:**
        - Try to use the STAR method (Situation, Task, Action, Result) for behavioral questions to ensure a well-structured and complete answer.
        """

        # Removed 'timeout=120'
        response = model.generate_content(prompt)

        if response.text:  # Check if response.text is not empty or None
            return response.text
        else:
            # If response.text is empty, but no exception was raised, something else went wrong
            st.warning(
                "Gemini returned an empty response. This might indicate an issue with the prompt or model availability.")
            # Also print the full response object to the console for more info
            print("Gemini API returned an empty text response. Full response object:", response)
            return "No feedback could be generated. Gemini returned an empty response. Please try again."

    except genai.types.BlockedPromptException as e:
        # Catch specific content policy violations
        st.error(f"❌ Gemini API blocked the prompt or response due to content policy: {e}")
        st.info("This usually happens if the input or generated content violates safety guidelines.")
        return "Feedback generation blocked due to content policy. Please try rephrasing your answer."
    except Exception as e:
        # Catch any other general exceptions during the API call
        st.error(
            f"❌ An error occurred while communicating with Gemini API: {e}. Please check your internet connection or try again.")
        st.info(
            "Possible causes: network issue, invalid API key (though found, might be revoked/incorrect), or model capacity.")
        return f"An error occurred while getting feedback: {e}"