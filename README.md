# 🎭 Poetry Agent with Roman Urdu Analysis

Welcome to the **Poetry Agent App**, an AI-powered poetry experience built with [Chainlit](https://www.chainlit.io/) and Google Gemini API (OpenAI-compatible). It beautifully crafts **2-stanza poems in Roman Urdu** and intelligently analyzes them through specialized analyst agents.

> **✨ Created by: Rahat Bano**

---

## 📜 Features

- ✍️ **Roman Urdu Poem Generation** – Automatically generates 2-stanza poems in Roman Urdu based on emotional or poetic prompts.
- 🔍 **Poem Type Detection** – Detects whether the poem is **lyric**, **narrative**, or **dramatic**.
- 🧠 **Expert Analysis Agents**:
  - 🎼 **Lyric Analyst** – Focuses on emotions, rhythm, and musicality.
  - 📖 **Narrative Analyst** – Analyzes plot, characters, and imagery.
  - 🎙️ **Dramatic Analyst** – Explores voice, dialogue, and performance.
- 🤖 Powered by **Gemini 2.0 Flash** via OpenAI-compatible API.

---

## 🚀 How It Works

1. **User Input** – You request a poem or provide one.
2. **Poetry Agent** – Generates or processes the poem in **Roman Urdu**.
3. **Orchestrator Agent** – Detects the poem type and routes it to the right analysis agent.
4. **Analyst Agents** – Provide deep analysis in **English**, even for Roman Urdu content.
5. **Chainlit UI** – Presents you the final poem and its analysis.

---

## 🛠️ Installation

### 1. Clone the Repository
git clone https://github.com/RahatBano58/Poetry-Agent.git
cd Poetry-Agent

### 2. Set Up Virtual Environment
uv venv
.venv\Scripts\activate

### 3. Set Environment Variables
GEMINI_API_KEY=your_google_gemini_api_key
OPENAI_API_KEY=your_openai_api_key

---

### 🧪 Running the App
chainlit run main.py
Open your browser to the URL provided by Chainlit (usually http://localhost:8000).

---

### 🧠 Project Structure

├── main.py               # Main Chainlit app with agents orchestration
├── connection.py         # API configuration with Gemini (OpenAI-compatible)
├── .env                  # API key (not committed)
└── README.md             # You are here 😄

---

### 📦 Dependencies
- chainlit
- python-dotenv
- agents-sdk (your custom SDK)
- openai (for Gemini-compatible client)


---

### 🙌 Created By
👩‍💻 **Rahat Bano**
Passionate about AI agents, poetry, and beautiful human-computer interaction. 💖
