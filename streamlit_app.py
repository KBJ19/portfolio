import streamlit as st
from utils import generate_response  # using HuggingFace-powered response

st.set_page_config(page_title="Khushal Jhaveri | Portfolio", layout="wide")

st.sidebar.title("📁 Navigation")
st.sidebar.page_link("pages/About.py", label="About Me")
st.sidebar.page_link("pages/Experience.py", label="Experience")
st.sidebar.page_link("pages/Projects.py", label="Projects")
st.sidebar.page_link("pages/Blog.py", label="Blog")
st.sidebar.page_link("pages/Contact.py", label="Contact")

st.title("🤖 Chat with Khushal")

st.markdown("""
Greetings, Human! 👋 I'm an AI trained to answer questions about Khushal's projects, experience, and journey. Ask me anything!
""")

user_query = st.text_input("What would you like to know?", placeholder="Try: What are Khushal's best projects?")

if user_query:
    with st.spinner("Thinking..."):
        response = generate_response(user_query)
        st.success(response)

st.markdown("**Quick Questions:**")
cols = st.columns(4)
quick_prompts = [
    "Who is Khushal?",
    "What are Khushal's skills?",
    "What are Khushal's achievements?",
    "How can I contact Khushal?"
]

for i, prompt in enumerate(quick_prompts):
    if cols[i].button(prompt):
        response = generate_response(prompt)
        st.success(response)
