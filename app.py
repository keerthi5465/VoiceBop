from flask import Flask, render_template, request, jsonify
from command_processor import CommandProcessor
from text_to_speech import speak

# Predefined commands
COMMANDS = {
    "open youtube": "Opening YouTube...",
    "open google": "Opening Google...",
    "what is your name": "I am your voice assistant.",
    "hello": "Hello! How are you?",
    "play songs": "Playing your favorite songs...",
    "kasaru": "Haha, I heard you say kasaru!",
    "stop it": "Okay, stopping now.",
    "exit": "Exiting voice command system."
}

app = Flask(__name__)
processor = CommandProcessor(COMMANDS)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_command():
    """Process command sent from browser mic"""
    data = request.get_json()
    command = data.get("command", "").lower().strip()
    response = processor.process(command)

    # ✅ Speak response on server (safe now)
    speak(response)

    return jsonify({"command": command, "response": response})

if __name__ == "__main__":
    app.run(debug=True)
