# Tutorix - AI-Powered Tutor Chatbot

## Team Name
LLMATES

## Team Members
- **Jamshed Ali Solangi (Lead)**: AI Software Engineer focused on Generative and Agentic AI. Experienced in building scalable AI applications using LangChain, LangGraph, and RAG pipelines. Handles AI integration and model design.
- **Muskan Ali Rizvi (Member)**: Final-year Software Engineering student and AI/Data Science enthusiast. Skilled in ML/DL and developing AI-powered solutions with LangChain, LangGraph, and RAG. Focuses on data processing and application logic.

## Project Title
AI-Powered Tutor Chatbot

## Category
Education

## Problem Statement
Develop an AI chatbot that answers questions in subjects like Math, Science, or History and explains each concept clearly, step-by-step. Students often need on-demand help with learning. Traditional tutoring can be expensive or unavailable. There is a need for an interactive, personalized, and context-aware learning tool.

## Solution
Tutorix is an AI-powered chatbot that:
- Provides step-by-step explanations tailored to student level (Beginner, Intermediate, Advanced)
- Supports context-aware answers using uploaded lecture notes (PDFs)
- Covers multiple subjects: Math, Science, History, Data Science, AI
- Allows saving and loading chat sessions
- Interactive and user-friendly interface built with Streamlit

**Workflow:**
1. Select subject, class level, and understanding level
2. Upload lecture notes (optional) for context-aware answers
3. Ask questions → AI responds clearly and step-by-step
4. Save/load chat sessions

## Unique Value
- Personalized step-by-step guidance
- Context-aware answers from uploaded notes
- Multi-subject support
- Chat session save/load
- Fast, on-demand learning

## Tech Stack
- Languages: Python
- Libraries: Streamlit, Python-dotenv, LangChain, LangChain-community, LangChain-HuggingFace, FAISS, Sentence-Transformers, PyPDF2
- AI Model: Llama-4-Scout via Cerebras API
- Tools: GitHub, JSON storage for sessions

## Setup Instructions
1. Clone the repository:  
   `git clone https://jamshedali18/LLmates-AI-Powered-Tutor-Chatbot.git`
2. Navigate to project folder:  
   `cd LLmates-AI-Powered-Tutor-Chatbot`
3. Install dependencies:  
   `pip install -r requirements.txt`
4. Set environment variables in a `.env` file:  
   `LLAMA_API_KEY=your_api_key_here`
5. Run the app:  
   `streamlit run main.py`

## Challenges Faced
- Processing large PDFs efficiently → Limited pages & chunking for vector store
- Context-aware AI responses → FAISS vector store for relevant content retrieval
- Maintaining conversation flow → Session state management in Streamlit

## Learnings
- Practical experience with LangChain & RAG pipelines
- Integrating AI models with Streamlit for real-time interaction
- Building context-aware educational chatbots
- Managing session state and file-based chat storage

## License
MIT License
