import requests
import streamlit as st

def generate_response(query):
    try:
        context = st.secrets["context"]["khushal"]
    except Exception as e:
        return f"❌ Could not load context from secrets: {e}"

    prompt = f"{context.strip()}\n\nUser: {query}\nKhushal’s AI Assistant:"

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xl"
    headers = {
        "Authorization": f"Bearer {st.secrets['huggingface']['HF_TOKEN']}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {"max_length": 300, "do_sample": False},
        "options": {"wait_for_model": True}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print("Status:", response.status_code)
        print("Text:", response.text)

        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return f"⚠️ Unexpected model response format: {result}"
    except Exception as e:
        return f"❌ Error: {e} — or model may be warming up."
