Legal Assistant — Local AI Chatbot (Ollama + FastAPI)
This project is a simple legal‑awareness chatbot using:

FastAPI backend

HTML/CSS/JS frontend

Ollama Llama 3 model (local AI, no API key needed)

The chatbot runs 100% locally — NO API keys required.

Requirements
Before running this project, install:

1. Python 3.10+
Download from: https://www.python.org

2. Ollama
Download from: https://ollama.com

After installing Ollama, download a model:

ollama pull llama3
(Or smaller model)

ollama pull llama3.2:3b
   Project Structure
legal-assistant/

│── index.html        ← Frontend
│── main.py           ← backend
│── .venv/            ← Python virtual environment (optional)
│── README.md         ← You are reading this :)
You only need index.html and main.py.

The .venv folder does NOT need to be shared unless required.

Installation Steps
1. Create a Virtual Environment
(optional but recommended)

python -m venv .venv
Activate it:

Windows:

.venv\Scripts\activate
2. Install dependencies
pip install fastapi uvicorn openai
3. Start Ollama
Ollama runs automatically in background, but if not:

ollama serve
4. Run the backend
uvicorn main:app --reload
Backend runs at:

👉 http://127.0.0.1:8000

   Frontend (index.html)
Right‑click → "Open with Live Server"
(or open it directly in your browser)

   The AI Model
This uses:

model = "llama3"
Since it runs locally via Ollama, no API key is needed.

 Done!
You can now type questions in the frontend and get answers from your local Llama model.
