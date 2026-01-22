import os
from groq import Groq
from dotenv import load_dotenv
from backend.prompt_templates import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_decision(decision_text: str):
    prompt = USER_PROMPT_TEMPLATE.format(decision=decision_text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
