Legal Assistant — Local AI Chatbot (Ollama + FastAPI)

A fully offline, privacy‑friendly chatbot that helps students and everyday people understand real‑life situations in simple, general legal language.
Runs 100% locally using Ollama, FastAPI, and a HTML/CSS/JS frontend — no API keys needed, and no internet required after installation.

Features:
Runs completely offline (Ollama local models)
Zero data sent to cloud — all processing happens on your device
Fast responses using local Llama 3 models
Lightweight session system (remembers your conversation until reset)
Upload support (images / documents) for context (optional if implemented)
Multi‑agent architecture (if added) — e.g., explainer agent, safety agent
Built‑in evaluation & logs (if included in your backend)

Requirements
Install these before running the project:

1. Python 3.10+
Download:
https://www.python.org/downloads/
Make sure to check “Add Python to PATH” during installation.

2. Ollama (Local AI Engine)
Download:
https://ollama.com/download

After downloading Ollama, install a model:

Best quality (recommended)
ollama pull llama3.1:8b
Smaller / faster alternatives
ollama pull llama3.2:3b (There in the code)
ollama pull phi3

Project Structure:
legal-assistant/
│── index.html       ← Frontend  
│── main.py          ← Backend  
│── README.md        ← Documentation  
│── .venv/           ← Virtual environment (DO NOT upload)
You only need index.html and main.py to run the app.

Installation & Setup:
1. Create a virtual environment (optional but recommended)
python -m venv .venv

Activate it:
Windows:
.venv\Scripts\activate

Mac/Linux:
source .venv/bin/activate

2. Install dependencies
pip install fastapi uvicorn openai
(The openai package is only used as a client — you are NOT using OpenAI API.)

3. Start Ollama
Ollama usually starts automatically.
If not, run:
ollama serve

4. Run the backend
uvicorn main:app --reload

Backend now runs at:
http://127.0.0.1:8000

5. Open the frontend
Open index.html in any browser.

If you use VS Code:
Right‑click → Open with Live Server

AI Model Used:
The backend loads:
model = "llama3.1:8b"

Since you are using Ollama:
No API keys required
No cloud services
100% private
Works offline once installed

Troubleshooting:

Backend doesn’t start?
Run:
pip install fastapi uvicorn openai

Model not found?
Run:
ollama pull llama3.2:3b

Frontend cannot connect?
Make sure backend is running at:
http://127.0.0.1:8000

You're all set!
You can now chat with your offline Legal Awareness Assistant.

