import pyttsx3

# Initialize engine once
engine = pyttsx3.init()

def speak(text: str):
    """
    Converts text to speech using pyttsx3.
    """
    engine.say(text)
    engine.runAndWait()


# ---------------- Test / Demo ----------------
if __name__ == "__main__":
    speak("Hello! This is your voice assistant speaking.")
    speak("You can integrate this with your command processor.")
