import pyttsx3

def speak(text):
    """
    Speak the given text using pyttsx3.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
