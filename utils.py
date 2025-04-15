import google.generativeai as genai
import streamlit as st

# Load the Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["gemini"]["API_KEY"])

# You can change this to any other valid model you listed earlier
MODEL_NAME = "gemini-1.5-pro"

def generate_response(query):
    try:
        # Use Gemini model
        model = genai.GenerativeModel(MODEL_NAME)

        # If you're using context, load it from file
        with open("khushal_ai_assistant_context.txt", "r", encoding="utf-8") as f:
            context = f.read()

        # Combine with query
        prompt = f"{context}\n\nUser: {query}\nKhushal’s AI Assistant:"

        # Generate response
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"❌ Error: {e}"
