# 😂 Joke AI Agent

A simple AI-powered Joke Generator built using Python, Streamlit, and OpenRouter LLM API with a smart fallback system using a local joke database.

The agent detects user intent and responds only with jokes. If the API fails or rate limit is exceeded, it automatically switches to local jokes.

---
# LIVE LINK

 - https://joke-agent-rnmkr4bc2v5bby65jjt63q.streamlit.app/

 ---

# 🚀 Features

- 🤖 AI-powered joke generation using OpenRouter LLM
- 😂 40+ built-in jokes (4 categories × 10 jokes each)
- 🧠 Smart joke category detection (tech, school, dad, funny)
- 🔁 No-repeat joke system
- ⚡ Automatic fallback to local jokes when API fails
- 🎨 Interactive Streamlit chat UI
- ⏳ Typing animation + loading spinner
- 🔒 Strict “joke-only” mode (blocks non-joke queries)

---

# 🧠 How It Works

User Input  
↓  
Intent Detection (joke or not)  
↓  
If joke request:  
- Try LLM (OpenRouter API)  
- If API fails → fallback to local jokes  
↓  
Response returned in Streamlit UI  

---




# ⚙️ Installation
# 1. Clone the repository
git clone https://github.com/sumit0991/Joke-Agent.git
cd joke-ai-agent
# 2. Install dependencies
pip install -r requirements.txt
# 3. Set up environment variables

--- 

# Create a .env file:

OPENROUTER_API_KEY=your_api_key_here

---

# ▶️ Run the App
streamlit run app.py


---

# 🧩 Tech Stack

- Python 🐍
- Streamlit 🎈
- OpenRouter API 🤖
- Requests 🌐

---

# 🔥 Key Concepts Used

- LLM API integration
- Prompt engineering (strict system prompt)
- Fallback architecture (LLM + local system)
- Intent classification (rule-based)
- State management (session + file memory)
- Streamlit UI design