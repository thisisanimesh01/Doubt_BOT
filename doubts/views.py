from django.shortcuts import render
from google.generativeai import configure
from .utils import get_gemini_answer

# Hardcoded Gemini API key (for testing only)
GEMINI_API_KEY = "AIzaSyAFZCiwjS-0UvBPxNMgWFxcv6l_3U1zazw"

def home(request):
    answer = ""
    question = ""

    # Configure Gemini API client with your key
    configure(api_key=GEMINI_API_KEY)

    if request.method == "POST":
        question = request.POST.get("question", "").strip()
        if question:
            answer = get_gemini_answer(question)

    return render(request, "doubts/home.html", {"answer": answer, "question": question})
