import requests
import streamlit as st

def generate_response(query):
    with open("khushal_ai_assistant_context.txt", "r") as f:
    context = f.read()


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
        print("Status Code:", response.status_code)
        print("Raw Response:", response.text)

        result = response.json()
        return result[0]["generated_text"]
    except Exception as e:
        return f"Error: {e} or model may be warming up."
