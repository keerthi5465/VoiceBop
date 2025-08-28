import speech_recognition as sr

def recognize_speech_from_mic():
    """
    Captures audio from the microphone and converts it to text using Google Speech Recognition.
    Returns the recognized text in lowercase.
    """
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # handle background noise
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""


# ---------------- Test / Demo ----------------
if __name__ == "__main__":
    while True:
        command = recognize_speech_from_mic()
        if command:
            print(f"You said: {command}")
        else:
            print("No command recognized.")
