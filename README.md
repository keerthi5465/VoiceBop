# 🔊 Voice Search System using Trie

## 📌 Overview

The **Voice Search System using Trie** is a voice-activated application that processes spoken commands, converts them to text, and efficiently matches them using a **Trie (prefix tree)**. It's designed for virtual assistants, smart devices, and accessibility tools, with features such as autocomplete, fuzzy matching, and command execution. This system offers fast prefix-based search and robustness against noisy inputs.

---

## 🎯 Key Objectives

- Capture and convert **voice input** to text using speech-to-text technology.
- Use a **Trie** for efficient command storage and matching.
- Handle **misrecognized inputs** with suggestions and fuzzy matching.
- Provide **responses via voice or text**.
- Add optional features like **web interface, API integration**, and **custom commands**.

---

## 🛠️ Core Features

- 🎙️ Record voice input via microphone.
- 🔤 Convert speech to text using libraries/APIs.
- 🌲 Match input using a Trie (prefix tree).
- ⚡ Trigger predefined actions for recognized commands.
- ❌ Handle errors gracefully (e.g., "weathr" → "weather").

---

## 💡 Extra Features

- 🧠 **Autocomplete**: Suggest complete commands from partial input.
- 🧩 **Fuzzy Matching**: Use Levenshtein distance for similar words.
- 🔁 **Text-to-Speech**: Voice output for responses.
- 🌐 **Web Interface**: Built with Flask + HTML/JS for interaction.
- ☁️ **API Integration**: Connect to services like OpenWeatherMap.

---

## 🧪 Implementation Overview

### Trie Data Structure

**Structure**:
Each node stores a character and tracks whether it ends a word.

**Key Operations**:
- `insert(word)`: Adds word to Trie.
- `search(word)`: Checks for complete command.
- `starts_with(prefix)`: Supports autocomplete.
- `fuzzy_match(word)`: Suggests corrections (optional).

## 🧰 Tech Stack

| Component       | Technology                                   |
| --------------- | -------------------------------------------- |
| Language        | Python                                       |
| Speech-to-Text  | `speech_recognition`, Google API             |
| Text-to-Speech  | Google TTS                                   |
| Web Interface   | Flask, HTML/CSS/JS                           |
| APIs (optional) | Google Custom Search                         |
| Dev Tools       | VS Code, PyCharm, Git, GitHub                |


## ✅ Challenges & Solutions
| Challenge              | Solution                                  |
| ---------------------- | ----------------------------------------- |
| Noisy speech input     | Use Google API or denoise using `librosa` |
| Trie memory usage      | Limit commands, compress Trie if needed   |
| Integration complexity | Use modular code and thorough testing     |
| Demo reliability       | Include text input fallback for testing   |


## 📈 Why This Project?
💡 Technical Depth: Implements Trie, optional fuzzy matching, voice-text systems.

🧠 Practical Relevance: Applies to AI, IoT, virtual assistants.

🎨 Engaging Demo: Interactive and voice-controlled interface.

🔄 Scalable: Easily extendable with APIs, multilingual support, analytics.

## 🚀 Getting Started
1.Clone Repository:
git clone https://github.com/your-username/voice_search_system.git
cd voice_search_system
2.Install Dependencies:
pip install -r requirements.txt
3.Run App (Console Mode):
python app.py

