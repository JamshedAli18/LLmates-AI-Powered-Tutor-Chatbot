# tutor_chain.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize Chat Model
model = ChatOpenAI(
    model="llama-4-scout-17b-16e-instruct",
    openai_api_key=os.getenv("LLAMA_API_KEY"),
    openai_api_base="https://api.cerebras.ai/v1",
    temperature=1.2
)

def build_prompt(subject, level, understanding, has_notes, context, question):
    """Dynamic prompt for AI tutor"""
    note_info = (
        "The student has uploaded lecture notes; use them as a primary reference."
        if has_notes else
        "The student did not upload any notes; answer based on your knowledge."
    )

    return f"""
You are an AI tutor specialized in {subject}.
The student is at the {level} level and has a {understanding} understanding of this topic.
{note_info}

Provide a clear, simple, and step-by-step explanation that matches the student's level.

Context (from uploaded notes if available):
{context}

Question:
{question}
"""

def get_tutor_response(prompt):
    """Generate response from AI model"""
    return model.invoke(prompt)
