import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
You are an AI Road Emergency Helpline Agent.
Your job is to:
- Calm the user
- Understand road emergencies (accidents, breakdowns, tyre burst, engine failure)
- Ask minimal clarification questions if needed
- Give clear instructions
- Inform that help is being dispatched to NHAI / emergency services
Keep responses short, reassuring, and authoritative.
"""

def get_ai_response(user_query: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_query}
            ],
            temperature=0.4,
            max_tokens=200
        )

        return completion.choices[0].message.content

    except Exception:
        return (
            "I’m here with you. Please stay calm and contact local emergency services immediately."
        )
