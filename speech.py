import logging
import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
import pyjokes
import pyaudio                     

from flask import Flask, request, render_template, jsonify

# Initialize Flask
app = Flask(__name__)

# Initialize recognizer
r = sr.Recognizer()
def spktxt(timeout=5, phrase_time_limit=6):
    """
    Listen on the server's microphone and return recognized text.
    Note: This listens on the machine where Flask runs (not the browser).
    """
    try:
        with sr.Microphone() as source:
            app.logger.info("Listening (server mic)...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            app.logger.info("Recognizing...")
            text = r.recognize_google(audio, language="en-IN")
            app.logger.info("Recognized: %s", text)
            return text
    except sr.WaitTimeoutError:
        return None
    except sr.UnknownValueError:
        return None
    except Exception as e:
        app.logger.exception("spktxt error:")
        return None


def speechtxt(text):
    """Speak text using pyttsx3."""
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")

        if len(voices) > 1:
            engine.setProperty("voice", voices[1].id)
        else:
            engine.setProperty("voice", voices[0].id)

        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        app.logger.exception("TTS error:")
        pass
@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    spoken_text = ""

    if request.method == "POST":
        # server microphone capture
        spoken_text = spktxt()

        if not spoken_text:
            output = "Sorry, I didn't catch that."
        else:
            data = spoken_text.lower()

            if "your name" in data:
                output = "I am a large language model Electronic Machine"

            elif "open youtube" in data:
                output = "Opening YouTube"
                webbrowser.open("https://www.youtube.com/")

            elif "joke" in data:
                output = pyjokes.get_joke(language="en", category="neutral")

            elif "time" in data:
                output = datetime.datetime.now().strftime("%I:%M %p")

            elif "exit" in data or "bye" in data or "quit" in data:
                output = "Thank you. Goodbye!"

            else:
                output = "Command not recognized."

            # Speak output
            speechtxt(output)

    return render_template("index.html", response=output, sptext=spoken_text)


#send to server
@app.route('/recognize', methods=['POST'])
def recognize_text():
    """
    This endpoint is used when the user clicks:
    'Send to Server' -> JavaScript sends text using fetch()
    """
    data = request.get_json() or {}
    user_text = data.get("text", "").strip()

    if not user_text:
        return jsonify({"success": False, "error": "No text received"}), 400

    lower = user_text.lower()

    # SAME COMMAND LOGIC AS ABOVE
    if "your name" in lower:
        reply = "I am a large language model Electronic Machine"

    elif "open youtube" in lower:
        reply = "Opening YouTube"
        webbrowser.open("https://www.youtube.com/")

    elif "joke" in lower:
        reply = pyjokes.get_joke(language="en", category="neutral")

    elif "time" in lower:
        reply = datetime.datetime.now().strftime("%I:%M %p")

    elif "exit" in lower or "quit" in lower or "bye" in lower:
        reply = "Thank you. Goodbye!"

    else:
        reply = f"I heard: {user_text}"

    # SPEAK REPLY
    speechtxt(reply)

    return jsonify({
        "success": True,
        "transcript": user_text,
        "reply": reply
    })
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
