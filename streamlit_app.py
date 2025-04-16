import streamlit as st
from utils import generate_response

st.set_page_config(page_title="Chat with Khushal", layout="wide")

# Inject floating hint for sidebar
st.markdown("""
    <style>
    .popup-hint {
        position: fixed;
        top: 70px;
        left: 20px;
        background-color: #111827;
        color: #fff;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 14px;
        z-index: 999;
        box-shadow: 0px 0px 8px rgba(0,0,0,0.3);
        animation: blink 1.5s infinite;
    }

    @keyframes blink {
        0%   { opacity: 1; }
        50%  { opacity: 0.4; }
        100% { opacity: 1; }
    }
    </style>

    <div class="popup-hint">
        👈 Click here to explore more about me!
    </div>
""", unsafe_allow_html=True)

# Title and intro
st.title("🤖 Chat with Khushal")
st.markdown("Greetings, Human! 👋 I'm an AI trained to answer questions about Khushal's projects, experience, and journey. Ask me anything!")

# Input box
query = st.text_input("What would you like to know?", placeholder="Try: What are Khushal's best projects?")

# Quick buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Who is Khushal?"):
        query = "Who is Khushal?"
with col2:
    if st.button("What are Khushal's skills?"):
        query = "What are Khushal's skills?"
with col3:
    if st.button("What are Khushal's achievements?"):
        query = "What are Khushal's achievements?"
with col4:
    if st.button("How can I contact Khushal?"):
        query = "How can I contact Khushal?"

# Output
if query:
    with st.spinner("Thinking..."):
        response = generate_response(query)
        st.success(response)
