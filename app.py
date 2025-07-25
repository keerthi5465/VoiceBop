from command_processor import CommandProcessor
from speech_to_text import recognize_speech_from_mic
from text_to_speech import speak

COMMANDS = ["play", "pause", "search", "weather", "stop"]

def main():
    processor = CommandProcessor(COMMANDS)
    while True:
        print("Say a command (or 'exit' to quit):")
        text = recognize_speech_from_mic()
        if not text:
            continue
        if text.lower() == "exit":
            break
        response = processor.process(text)
        print("Response:", response)
        speak(response)

if __name__ == "_main_":
    main()