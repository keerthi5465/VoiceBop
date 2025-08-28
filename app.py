# app.py
from command_processor import CommandProcessor
import speech_recognition as sr

# Predefined commands and their responses
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

def main():
    processor = CommandProcessor(COMMANDS)
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        print("\nSay a command (or 'exit' to quit):")
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
            response = processor.process(command)
            print(f"Response: {response}")

            if command.lower().strip() == "exit":
                break

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
