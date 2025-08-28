🔊 Voice Search System using Trie
📌 Overview

The Voice Search System using Trie is a voice-activated application that captures spoken commands, converts them to text, and efficiently matches them using a Trie (prefix tree). It is designed for virtual assistants, smart devices, and accessibility tools, featuring autocomplete, fuzzy matching, and command execution. The system provides fast prefix-based search and is robust against noisy or partial inputs.

🎯 Key Objectives

Capture and convert voice input to text using speech-to-text technology.

Store and match commands efficiently using a Trie.

Handle misrecognized inputs with suggestions or fuzzy matching.

Provide responses via text and voice.

Optional enhancements: web interface, API integration, custom commands.

🛠️ Core Features

🎙️ Record voice input via microphone.

🔤 Convert speech to text using Python libraries/APIs.

🌲 Match input using a Trie (prefix tree).

⚡ Trigger predefined actions for recognized commands.

❌ Handle errors gracefully (e.g., "weathr" → "weather").

💡 Extra Features

🧠 Autocomplete: Suggest complete commands from partial input.

🧩 Fuzzy Matching: Use Levenshtein distance for approximate matches.

🔁 Text-to-Speech: Voice output for responses.

🌐 Web Interface: Flask + HTML/JS for browser interaction.

☁️ API Integration: Connect to services like OpenWeatherMap.

🛠️ Custom Commands: Allow users to define new commands.

🧠 Context-Aware Matching: Prioritize frequent commands.

🌍 Multilingual Support: Extend commands in multiple languages.

📊 Analytics Dashboard: Track command usage statistics.

🧰 Tech Stack
Component	Technology
Language	Python
Speech-to-Text	speech_recognition, Google Speech API
Text-to-Speech	pyttsx3 (offline), Google TTS (optional)
Web Interface	Flask, HTML/CSS/JS, WebRTC
APIs	OpenWeatherMap, Google Custom Search
📈 Why This Project?

💡 Technical Depth: Implements Trie, optional fuzzy matching, and voice-text systems.

🧠 Practical Relevance: Applies to AI, IoT, and virtual assistants.

🎨 Engaging Demo: Interactive and voice-controlled interface.

🔄 Scalable: Easily extendable with APIs, multilingual support, and analytics.

🚀 Getting Started
1. 🔁 Clone the Repository
git clone https://github.com/keerthi5465/VoiceBop
cd voice_search_system

2. 📦 Install Dependencies
pip install -r requirements.txt


⚠️ Make sure pyaudio is installed properly for microphone support. On Windows, you may need the precompiled wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
.

3. ▶️ Run the Application (Console Mode)
python app.py


Say a command into your microphone.

Type exit to quit the application.

Supported commands by default: "play", "pause", "search", "weather", "stop".

4. 🧪 Optional: Run Tests
python -m unittest discover tests


Verifies Trie, command processor, autocomplete, and fuzzy matching.