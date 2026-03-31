Visit - https://agenticchatfloow.streamlit.app/

# 🤖 AgenticChatFlow

An end-to-end **AI Agent application** built using **LangGraph, Streamlit, and FastAPI**, with support for **Groq/OpenAI models** and optional **real-time web search integration**.

---

## 🚀 Overview

AgenticChatFlow is a powerful AI-driven conversational application designed to provide intelligent, context-aware responses using modern agentic workflows.

This project combines:
- **LangGraph** for agent orchestration
- **FastAPI** for backend APIs
- **Streamlit** for interactive frontend UI
- **Groq / OpenAI LLMs** for fast and intelligent responses
- **Web Search integration** for real-time information retrieval

The application follows an end-to-end pipeline from user query → AI agent reasoning → response generation → frontend display.

---

## 🛠️ Tech Stack

- **Python**
- **LangGraph**
- **LangChain**
- **Streamlit**
- **FastAPI**
- **Groq API**
- **OpenAI API**
- **Uvicorn**
- **REST APIs**

---

## 📂 Project Structure

```bash
AgenticChatFlow/
│
├── ai_agent.py          # AI agent workflow logic
├── backend.py           # FastAPI backend server
├── frontend.py          # Streamlit frontend UI
├── main.py              # Main execution file
├── requirements.txt     # Required dependencies
├── pyproject.toml       # Project configuration
└── .gitignore
```

---

## ⚙️ Features

- ✅ End-to-end AI Agent workflow
- ✅ Multi-step reasoning with LangGraph
- ✅ FastAPI backend integration
- ✅ Streamlit interactive UI
- ✅ Supports Groq & OpenAI models
- ✅ Real-time response generation
- ✅ Scalable and modular architecture
- ✅ Optional web search support

---

## 💡 How It Works

1. User enters query in **Streamlit UI**
2. Query is sent to **FastAPI backend**
3. **LangGraph agent** processes the request
4. LLM generates intelligent response
5. Final response is displayed on frontend

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Aayushkumar51/AgenticChatFlow.git
cd AgenticChatFlow
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Start Backend

```bash
uvicorn backend:app --reload
```

### Start Frontend

```bash
streamlit run frontend.py
```

---

## 🎯 Use Cases

- AI Chatbot Systems
- Agentic Workflows
- LLM Applications
- Real-time Search Assistants
- Customer Support Bots
- Intelligent Query Systems

---

## 📈 Future Improvements

- Multi-agent collaboration
- Memory-based conversations
- RAG integration
- Deployment on Render / Streamlit Cloud
- Authentication system

---

## 👨‍💻 Author

**Ayush Kumar**  
AI / ML Developer | Generative AI Enthusiast

GitHub: https://github.com/Aayushkumar51
