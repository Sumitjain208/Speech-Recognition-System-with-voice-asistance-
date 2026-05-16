Voice Assistant Flask Web App

A simple AI-powered Voice Assistant Web Application built using Python, Flask, Speech Recognition, and Text-to-Speech.
The assistant can listen to voice commands, speak responses, tell jokes, open websites, and perform basic tasks.

🚀 Features
🎤 Speech Recognition using microphone
🔊 Text-to-Speech response
😂 Tell jokes using PyJokes
⏰ Tell current time
🌐 Open YouTube in browser
🧠 Simple command-based assistant
💻 Flask Web Interface
📡 API endpoint for sending text commands
🛠️ Technologies Used
Python
Flask
SpeechRecognition
PyAudio
pyttsx3
PyJokes
📂 Project Structure
voice-assistant/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│
└── README.md
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
📦 Required Libraries
Flask
SpeechRecognition
pyttsx3
PyAudio
pyjokes
▶️ Run Application
python app.py

Server will start at:

http://127.0.0.1:5000
🎙️ Available Commands
Command	Action
"your name"	Tells assistant name
"open youtube"	Opens YouTube
"joke"	Tells a joke
"time"	Speaks current time
"bye" / "quit"	Exits assistant
🧠 How It Works
User clicks button on webpage
Flask captures voice from server microphone
SpeechRecognition converts speech to text
Assistant processes command
pyttsx3 converts reply into speech
Response shown on webpage
📡 API Endpoint
POST /recognize

Send text command to server.

Example Request
{
  "text": "open youtube"
}
Example Response
{
  "success": true,
  "transcript": "open youtube",
  "reply": "Opening YouTube"
}
⚠️ Important Note

This project listens through the server microphone, not the browser microphone.

If deployed online (Render, Railway, Streamlit, etc.), microphone functionality may not work because cloud servers do not have microphone access.

Best used on:

Local Machine
Personal Computer
Laptop
🖼️ Future Improvements
Browser microphone support
AI chatbot integration
Weather updates
Music player
Open applications
Voice authentication
Multi-language support
🤝 Contributing

Contributions are welcome.

Fork the repository
Create a new branch
Commit changes
Push code
Create Pull Request
📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by Sumit Jain 🚀

﻿# SpeechToText

A Python application for converting speech to text.

## Requirements
- Python 3.x
- Required packages (list them here)

## Setup
1. Clone the repository
2. Install dependencies
3. Run the script

## Usage
Describe how to use your application here
