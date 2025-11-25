Legal Assistant — Local AI Chatbot (Ollama + FastAPI)
A simple legal‑awareness chatbot that runs fully offline using:

FastAPI backend
HTML/CSS/JS frontend
Ollama (local AI models)
No API keys
No internet required after setup

Requirements (Install these before running)

1. Python 3.10+
Download from: https://www.python.org/downloads/
( Make sure to check “Add Python to PATH” during installation)

2. Ollama (Local AI engine)
Download from: https://ollama.com/download

After installing Ollama, download a model:
Recommended (best quality):
ollama pull llama3
Small model (if low storage):
ollama pull llama3.2:3b

 Project Structure
legal-assistant/
│── index.html        ← Frontend
│── main.py           ← Backend
│── README.md         ← Documentation
│── .venv/            ← Virtual environment (DO NOT upload)
You only need index.html and main.py to run the project.

 Installation Steps
1. Create a virtual environment
(optional but recommended)
python -m venv .venv

Activate it:

Windows:
.venv\Scripts\activate

Mac/Linux:
source .venv/bin/activate

2. Install dependencies
pip install fastapi uvicorn openai
(The “openai” package is used only as a client. You are NOT using OpenAI API.)

3. Start Ollama
(Ollama normally runs automatically)

If needed:
ollama serve

4. Run the backend
uvicorn main:app --reload

Your backend is now running at:
http://127.0.0.1:8000

Frontend (index.html)
Open it in your browser.

If using VS Code:
Right‑click → Open with Live Server

AI Model Used
The backend loads:
model = "llama3"
Since Ollama runs locally:
No API keys needed
No internet needed
100% private

Troubleshooting:

Backend doesn’t start?
Run:
pip install fastapi uvicorn openai

Model not found?
Run:
ollama pull llama3

Frontend not connecting?
Check that your backend is running at:
http://127.0.0.1:8000

Done!
You can now chat with your offline legal assistant.
