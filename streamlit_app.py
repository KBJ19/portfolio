import streamlit as st
from utils import generate_response

st.set_page_config(page_title="Chat with Khushal", layout="wide")

st.title("🤖 Chat with Khushal")
st.markdown("Greetings, Human! 👋 I'm an AI trained to answer questions about Khushal's projects, experience, and journey. Ask me anything!")

query = st.text_input("What would you like to know?", placeholder="Try: What are Khushal's best projects?")

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

if query:
    with st.spinner("Thinking..."):
        response = generate_response(query)
        st.success(response)
