# Voice Search System using Trie

## Project Overview
The Voice Search System using Trie is a Python-based application that processes voice inputs, converts them to text, and matches them to predefined commands or search terms stored in a Trie (prefix tree) data structure. The system can execute actions (like fetching data or triggering functions) or suggest corrections for misrecognized inputs, making it suitable for virtual assistants, smart devices, or accessibility tools.

## Key Features
- **Voice Input:** Record voice input via a microphone.
- **Speech-to-Text:** Convert voice to text using speech recognition.
- **Trie Command Matching:** Efficient command matching and autocomplete using a Trie.
- **Error Handling:** Suggest corrections for misrecognized or partial commands (autocomplete, fuzzy matching).
- **Text-to-Speech:** Provide responses via voice output.
- **Extensible:** Easily add new commands, API integrations, or a web interface.

## Architecture
```
User (Voice) → Speech-to-Text → Trie Command Processor → Action/Response → Text-to-Speech (Voice Output)
```

- **trie.py:** Implements the Trie data structure for command storage, search, autocomplete, and fuzzy matching.
- **speech_to_text.py:** Handles microphone input and converts speech to text.
- **text_to_speech.py:** Converts text responses to speech.
- **command_processor.py:** Matches recognized text to commands, executes actions, and handles errors.
- **app.py:** Main entry point; integrates all modules and runs the system.
- **templates/index.html:** (Optional) Web UI for voice input/output (Flask integration).
- **tests/**: Unit and integration tests for core modules.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd VoiceBop
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **(Optional) Run tests:**
   ```bash
   python -m unittest discover tests
   ```

## Usage
- Speak a command (e.g., "play", "search", "weather") into your microphone.
- The system will recognize your command, match it using the Trie, and execute the corresponding action.
- If the command is not recognized, the system will suggest similar or corrected commands.
- Responses are provided via text and voice output.

## Example Commands
- play
- pause
- search
- weather
- stop

## Extending the Project
- **Add More Commands:** Update the command list in `app.py` or `command_processor.py`.
- **API Integration:** Implement API calls (e.g., weather, search) in `command_processor.py`.
- **Web Interface:** Build out the Flask app and enhance `templates/index.html`.
- **Custom Commands:** Allow users to add commands via the UI or a configuration file.
- **Analytics:** Track and display command usage statistics.
- **Multilingual Support:** Store and match commands in multiple languages.

## Challenges and Solutions
- **Speech Recognition Accuracy:** Use Google Speech-to-Text for higher accuracy or preprocess audio for noise reduction.
- **Trie Scalability:** Limit the number of commands or optimize the Trie for large command sets.
- **Integration Complexity:** Use modular design and thorough testing.
- **Demo Environment:** Provide a text-based fallback mode for noisy environments.

## License
MIT License

---

**For questions or contributions, please open an issue or pull request!** 