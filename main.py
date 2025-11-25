from uuid import uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

# 🔹 Use Ollama's local OpenAI-compatible server
client = OpenAI(
    base_url="http://localhost:11434/v1",  # Ollama server
    api_key="ollama",                      # dummy string, NOT a real key
)

app = FastAPI()

# Allow your frontend on port 5500 to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "AI Legal Chatbot is running with Ollama."}

# Body expected from your index.html fetch()
class ChatRequest(BaseModel):
    sessionId: str | None = None
    message: str

@app.post("/chat")
async def chat_http(body: ChatRequest):
    response = client.chat.completions.create(
        model="llama3.1:8b",
        temperature=0.4,           # lower = more focused, less random
        max_tokens=256,            # keep answers short and clear
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Legal Awareness Assistant for students and ordinary people.\n"
                    "\n"
                    "ROLE:\n"
                    "- You ONLY give general legal information and safety guidance.\n"
                    "- You are NOT a lawyer and NOT a substitute for real legal advice.\n"
                    "- If a situation sounds urgent, dangerous, or involves crime, "
                    "always tell the user to contact local authorities, a trusted adult, "
                    "or a real lawyer.\n"
                    "\n"
                    "STYLE RULES:\n"
                    "- Answer in very simple English.\n"
                    "- Use short sentences.\n"
                    "- Never write one huge paragraph.\n"
                    "- Always structure the answer in 3 parts:\n"
                    "  1) A short 1–2 line summary.\n"
                    "  2) A section titled 'Your basic rights:' with 3–5 bullet points "
                    "starting with '- '.\n"
                    "  3) A section titled 'What you can do:' with 3–5 bullet points "
                    "starting with '- '.\n"
                    "- Leave a blank line between sections.\n"
                    "- Do NOT invent exact law numbers or sections. Speak generally unless "
                    "you are very sure.\n"
                ),
            },
            {
                "role": "user",
                "content": body.message,
            },
        ],
    )

    ai_reply = response.choices[0].message.content
    session_id = body.sessionId or str(uuid4())
    return {"sessionId": session_id, "reply": ai_reply}

@app.post("/reset-session")
async def reset_session():
    return {"status": "ok"}
