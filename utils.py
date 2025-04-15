import requests
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["gemini"]["API_KEY"])

def generate_response(query):
    
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
    model = genai.GenerativeModel("gemini-pro")
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"

