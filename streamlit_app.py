import streamlit as st
from utils import load_data, generate_response

st.set_page_config(page_title="Khushal Jhaveri | Portfolio", layout="wide")
st.sidebar.title("📁 Navigation")
st.sidebar.page_link("About", label="About Me")
st.sidebar.page_link("Experience", label="Experience")
st.sidebar.page_link("Projects", label="Projects")
st.sidebar.page_link("Blog", label="Blog")
st.sidebar.page_link("Contact", label="Contact")

st.title("🤖 Chat with Khushal")

st.markdown("""
Greetings, Human! 👋 I'm an AI trained to answer questions about Khushal's projects, experience, and journey. Ask me anything!
""")

user_query = st.text_input("What would you like to know?", placeholder="Try: What are Khushal's best projects?")

if user_query:
    with st.spinner("Thinking..."):
        data = load_data()
        response = generate_response(user_query, data)
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
        data = load_data()
        response = generate_response(prompt, data)
        st.success(response)
