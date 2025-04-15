import requests
import streamlit as st

def generate_response(query):
    try:
        with open("khushal_ai_assistant_context.txt", "r") as f:
            context = f.read()
    except FileNotFoundError:
        return "Error: Context file not found. Please make sure khushal_ai_assistant_context.txt exists."

    prompt = f"{context}\n\nUser: {query}\nKhushal’s AI Assistant:"

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    headers = {
        "Authorization": f"Bearer {st.secrets['huggingface']['HF_TOKEN']}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {"max_length": 200, "do_sample": False},
        "options": {"wait_for_model": True}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text}"

        result = response.json()
        return result[0]["generated_text"]
    except Exception as e:
        return f"Error: {e} or model may be warming up."
