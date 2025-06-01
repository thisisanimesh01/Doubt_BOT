import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-001")  # Use the appropriate model ID

def get_gemini_answer(question: str) -> str:
    prompt = f"Answer this question as if you are a friendly tutor: {question}"
    response = model.generate_content(prompt)
    return response.text
