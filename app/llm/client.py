from openai import OpenAI
from app.core.config import settings

AI_PIPE_BASE_URL = "https://aipipe.org/openai/v1" 

_client = OpenAI(
    base_url=AI_PIPE_BASE_URL,
    api_key=settings.openai_api_key or "missing"  # Ensure this contains your AIPipe Token
)

def generate(prompt: str) -> str:
    response = _client.chat.completions.create(
        model=settings.llm_model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content
