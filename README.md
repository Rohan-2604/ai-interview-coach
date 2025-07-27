# 🚀 AI Interview Coach

A web-based tool that helps users practice interview questions by analyzing their voice or text answers using Google's Gemini AI and providing structured feedback. This project showcases end-to-end product thinking, leveraging modern NLP, LLMs, and API integrations.

## ✨ Features (MVP Scope)

* **Text Input Box:** Users can type their interview answers.
* **Voice Input:** Capture voice answers from the user's microphone.
* **LLM-Based Feedback:** Utilizes Google's Gemini AI to analyze answers.
* **Structured Output:** Provides feedback on clarity, structure, tone, completeness, and optional technical coverage in bullet points.
* **Sample Questions:** Pre-loaded HR and technical interview questions.
* **(Local Only) Read Aloud Feature:** Converts AI feedback to speech for an auditory experience.

## 🛠 Tech Stack

* **Web Frontend:** Streamlit (for fast UI development)
* **Backend:** Python
* **AI Engine:** Google Gemini API (using `gemini-1.5-flash` or `gemini-1.5-pro` model)
* **Voice Input:** `speech_recognition` (for local microphone access with `PyAudio`)
* **TTS Output:** `pyttsx3` (for local text-to-speech)

## 🗂 File Structure

ai-interview-coach/
│
├── app.py                  # Main Streamlit application
├── ai_feedback.py          # Handles Gemini API interaction and feedback generation
├── questions.py            # Stores predefined interview questions
├── voice_input.py          # Manages voice input (speech-to-text) and TTS output
├── requirements.txt        # Python dependencies for pip
├── packages.txt            # System-level dependencies (e.g., for PyAudio on Linux-like systems)
├── README.md               # Project description and setup instructions (this file)
└── .gitignore              # Specifies files/folders to ignore in Git


## 🚀 Setup & Running Locally

Follow these steps to get the AI Interview Coach running on your local machine.

### **Step 1: Prerequisites**

* **Python 3.8+:** Download and install from [python.org](https://www.python.org/downloads/). Ensure "Add Python to PATH" is checked during installation.
* **Git:** Download and install from [git-scm.com](https://git-scm.com/downloads).
* **Google Gemini API Key:** You *must* obtain your own API key.
    1.  Go to [Google AI Studio](https://aistudio.google.com/).
    2.  Sign in with your Google Account.
    3.  Follow the prompts to generate a new API key (look for "Get API Key" or "API key" in the sidebar).
    4.  **Copy your API key immediately.**

### **Step 2: Clone the Repository**

Open your terminal or command prompt and clone this repository:

```bash
git clone [https://github.com/Rohan-2604/ai-interview-coach.git](https://github.com/Rohan-2604/ai-interview-coach.git)
cd ai-interview-coach


Step 3: Set Up a Python Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

Bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Step 4: Install Python Dependencies
With your virtual environment activated, install the required Python libraries:

Bash

pip install -r requirements.txt
Step 5: Configure Your Gemini API Key (Environment Variable)
For local development, the app expects your Gemini API key to be set as a system environment variable named GEMINI_API_KEY.

For Windows:

Search "Environment Variables" in the Windows search bar and select "Edit the system environment variables."

Click "Environment Variables..."

Under "User variables for [Your User Name]", click "New...".

Set "Variable name" to GEMINI_API_KEY.

Set "Variable value" to your actual Gemini API key.

Click "OK" on all windows.

Crucial: Close and reopen your terminal/PyCharm after setting this.

For macOS/Linux:

Open your terminal.

Edit your shell's profile file (e.g., ~/.bashrc, ~/.zshrc, or ~/.profile).

Add the following line to the end of the file, replacing YOUR_API_KEY_HERE with your actual key:

Bash

export GEMINI_API_KEY="YOUR_API_KEY_HERE"
Save and close the file.

Apply changes: source ~/.bashrc (or source ~/.zshrc).

Crucial: Close and reopen your terminal/PyCharm after setting this.

Step 6: Run the Streamlit Application
With your virtual environment still activated, run the app:

Bash

streamlit run app.py
This will open the AI Interview Coach in your default web browser (usually at http://localhost:8501).

Step 7: Microphone Permissions (For Voice Input)
For the voice input feature to work, your operating system and browser must grant microphone access to the running application.

Browser: When you click "Start Recording" for the first time, your browser will likely ask for microphone permission. Allow it.

Operating System (Windows): Go to Settings > Privacy & security > Microphone. Ensure "Microphone access," "Let apps access your microphone," and "Desktop app access to microphone" are all ON.

Note on Voice Input/Output on Cloud Deployment:
If you deploy this application to a cloud hosting platform, direct microphone input and text-to-speech using speech_recognition and pyttsx3 may not function due to server-side limitations in containerized environments. These features are best experienced in the local development environment.






give me a complete readme file i can just copy paste as it is


Markdown

# 🚀 AI Interview Coach

A web-based tool that helps users practice interview questions by analyzing their voice or text answers using Google's Gemini AI and providing structured feedback. This project showcases end-to-end product thinking, leveraging modern NLP, LLMs, and API integrations.

## ✨ Features (MVP Scope)

* **Text Input Box:** Users can type their interview answers.
* **Voice Input:** Capture voice answers from the user's microphone.
* **LLM-Based Feedback:** Utilizes Google's Gemini AI to analyze answers.
* **Structured Output:** Provides feedback on clarity, structure, tone, completeness, and optional technical coverage in bullet points.
* **Sample Questions:** Pre-loaded HR and technical interview questions.
* **(Local Only) Read Aloud Feature:** Converts AI feedback to speech for an auditory experience.

## 🛠 Tech Stack

* **Web Frontend:** Streamlit (for fast UI development)
* **Backend:** Python
* **AI Engine:** Google Gemini API (using `gemini-1.5-flash` or `gemini-1.5-pro` model)
* **Voice Input:** `speech_recognition` (for local microphone access with `PyAudio`)
* **TTS Output:** `pyttsx3` (for local text-to-speech)

## 🗂 File Structure

ai-interview-coach/
│
├── app.py                  # Main Streamlit application
├── ai_feedback.py          # Handles Gemini API interaction and feedback generation
├── questions.py            # Stores predefined interview questions
├── voice_input.py          # Manages voice input (speech-to-text) and TTS output
├── requirements.txt        # Python dependencies for pip
├── packages.txt            # System-level dependencies (e.g., for PyAudio on Linux-like systems)
├── README.md               # Project description and setup instructions (this file)
└── .gitignore              # Specifies files/folders to ignore in Git


## 🚀 Setup & Running Locally

Follow these steps to get the AI Interview Coach running on your local machine.

### **Step 1: Prerequisites**

* **Python 3.8+:** Download and install from [python.org](https://www.python.org/downloads/). Ensure "Add Python to PATH" is checked during installation.
* **Git:** Download and install from [git-scm.com](https://git-scm.com/downloads).
* **Google Gemini API Key:** You *must* obtain your own API key.
    1.  Go to [Google AI Studio](https://aistudio.google.com/).
    2.  Sign in with your Google Account.
    3.  Follow the prompts to generate a new API key (look for "Get API Key" or "API key" in the sidebar).
    4.  **Copy your API key immediately.**

### **Step 2: Clone the Repository**

Open your terminal or command prompt and clone this repository:

```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/ai-interview-coach.git](https://github.com/YOUR_GITHUB_USERNAME/ai-interview-coach.git)
cd ai-interview-coach
(Replace YOUR_GITHUB_USERNAME with your actual GitHub username).

Step 3: Set Up a Python Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

Bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Step 4: Install Python Dependencies
With your virtual environment activated, install the required Python libraries:

Bash

pip install -r requirements.txt
Step 5: Configure Your Gemini API Key (Environment Variable)
For local development, the app expects your Gemini API key to be set as a system environment variable named GEMINI_API_KEY.

For Windows:

Search "Environment Variables" in the Windows search bar and select "Edit the system environment variables."

Click "Environment Variables..."

Under "User variables for [Your User Name]", click "New...".

Set "Variable name" to GEMINI_API_KEY.

Set "Variable value" to your actual Gemini API key.

Click "OK" on all windows.

Crucial: Close and reopen your terminal/PyCharm after setting this.

For macOS/Linux:

Open your terminal.

Edit your shell's profile file (e.g., ~/.bashrc, ~/.zshrc, or ~/.profile).

Add the following line to the end of the file, replacing YOUR_API_KEY_HERE with your actual key:

Bash

export GEMINI_API_KEY="YOUR_API_KEY_HERE"
Save and close the file.

Apply changes: source ~/.bashrc (or source ~/.zshrc).

Crucial: Close and reopen your terminal/PyCharm after setting this.

Step 6: Run the Streamlit Application
With your virtual environment still activated, run the app:

Bash

streamlit run app.py
This will open the AI Interview Coach in your default web browser (usually at http://localhost:8501).

Step 7: Microphone Permissions (For Voice Input)
For the voice input feature to work, your operating system and browser must grant microphone access to the running application.

Browser: When you click "Start Recording" for the first time, your browser will likely ask for microphone permission. Allow it.

Operating System (Windows): Go to Settings > Privacy & security > Microphone. Ensure "Microphone access," "Let apps access your microphone," and "Desktop app access to microphone" are all ON.

Note on Voice Input/Output on Cloud Deployment:
If you deploy this application to a cloud hosting platform, direct microphone input and text-to-speech using speech_recognition and pyttsx3 may not function due to server-side limitations in containerized environments. These features are best experienced in the local development environment.