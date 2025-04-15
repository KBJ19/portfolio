import requests
import streamlit as st

# Shortened context (truncated from your full assistant background)
context = """
Khushal Jhaveri is a Master’s student in Computer Science at USC, specializing in AI. He's worked on real-world projects combining AI, vision, and language. Key work includes:

- Drone vision system at ResoluteAI using YOLOv8 and Streamlit dashboards
- Readability improvement of scanned textbooks for rural outreach using OpenCV
- Led marketing and fundraising for BloomBox, a student startup incubator
- Built a multimodal emotion detection model (MediaPipe + Librosa + NLP on MELD)
- Created medical ultrasound classifiers for gallbladder stone detection
- Developed LSTM-based Amazon review sentiment analysis
- Engineered a YouTube summarizer using OpenAI GPT + chunking
- Created a GAN-based sorting visualizer and vocabulary generator

Skills: Python, PyTorch, TensorFlow, OpenCV, Streamlit, YOLOv8, Hugging Face, prompt engineering.
"""

def generate_response(query):
    prompt = f"""{context}

User: {query}
Khushal’s AI Assistant:"""

    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

    headers = {
        "Authorization": f"Bearer {st.secrets['huggingface']['HF_TOKEN']}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 256, "do_sample": False},
        "options": {"wait_for_model": True}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print("Status Code:", response.status_code)
        print("Raw Response Text:", response.text)

        if response.status_code != 200 or not response.text.strip():
            return "⚠️ Model returned no content. It might be warming up or the prompt was too long."

        result = response.json()

        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            return result[0]["generated_text"].split("Khushal’s AI Assistant:")[-1].strip()
        else:
            return f"⚠️ Unexpected response format: {result}"
    except Exception as e:
        return f"❌ Error: {e} — or the model may be unavailable."
