import streamlit as st
from PIL import Image

st.set_page_config(page_title="About | Khushal Jhaveri", layout="wide")

# Layout: Profile image on left, content on right
col1, col2 = st.columns([1, 3], gap="large")
with col1:
    image = Image.open("assets/profile-pic (3).png")
    st.image(image, caption="Khushal Jhaveri", width=240)
    st.write("")  # Spacer to push content slightly downward

with col2:
    st.title("👋 About Me")
    st.write("""
Hi, I'm **Khushal Jhaveri** — currently pursuing my Master’s in Computer Science with a focus on Artificial Intelligence at the **University of Southern California (USC)**. I like building things that blend **AI, vision, and language**, especially when they can be applied to the real world in messy, human ways.

Over the past few years, I've been lucky to work on projects that go beyond just accuracy scores. Whether it was building a multimodal emotion detector using facial cues, audio, and text — or developing computer vision tools to improve blurry textbook scans for rural education — the goal has always been to make AI *feel* a little more useful, a little more human.

Before USC, I completed my B.Tech in Computer Engineering from K.J. Somaiya College in Mumbai, with an Honors in Cybersecurity. I was also the **Marketing Head of BloomBox**, our entrepreneurship cell, where I led large-scale events and funding efforts — which, by the way, taught me more about leadership than any classroom ever could.

I’ve worked as a **Deep Learning Engineer Intern at ResoluteAI**, leading proof-of-concept projects for clients involving drone imaging, YOLOv8 models, and traditional computer vision — sometimes ditching deep learning altogether when CV worked better. I’ve also interned at **Suvidha Foundation**, using OpenCV to enhance scanned educational material for underprivileged girls.

Outside of tech, I’ve worn many hats — fundraiser, speaker coordinator, pitch deck builder, and event host. I believe all of that shapes how I think about problem-solving today.
""")

st.markdown("---")

st.header("🌱 Things I'm exploring")
st.write("""
- Using AI for education and accessibility
- Low-cost healthcare tools via computer vision
- LLMs for summarization, creativity, and context-aware dialogue
- Cloud systems that scale smartly — I’m **Azure certified** too
""")

st.markdown("---")

st.header("💬 Outside the Resume")
st.write("""
I’m not just about code and models — I love putting myself out there.

I’ve hosted events, built sponsorship decks, run logistics for 1000+ people, and helped organize national startup summits. I enjoy learning how people think, what makes them tick, and how good design and tech can be a bridge between people and systems.

I’m an **extrovert**, but also someone who **likes going deep** — whether it’s a model architecture, a business deck, or an old-school martial arts kata. I learn best when I understand things thoroughly, and I ask a lot of “why’s” along the way.
""")

st.markdown("---")

st.header("☕ Interests Outside Tech")
st.write("""
- 🍜 **Food** — big-time foodie, always up to explore new places or cook something wildly experimental.
- 📸 **Photography** — mostly candid, street, and the occasional cloud obsession.
- 🚴‍♂️ **Cycling** — long night rides are my version of therapy.
- 🥋 **Martial Arts** — trained in it, practiced it, loved it.
- 🚗 **Cars** — both on road and under the hood. If it moves, I’m curious.
""")

st.markdown("---")

st.header("🧠 My current mindset")
st.write("""
I’m not chasing the fanciest solution — I want the **right** one. Whether that’s GANs or just clever thresholding in OpenCV, I enjoy going deep, failing a bit, iterating, and making something that works.

And if I can help someone else along the way — whether it’s through mentoring, collabs, or just open-source — that’s a bonus I’ll always take.

Thanks for reading all the way :) If any of that connects with you — feel free to reach out or check out my work across the other tabs.
""")

st.markdown("---")

# Social links
st.subheader("📬 Let's Connect")
st.markdown("""
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](http://www.linkedin.com/in/khushaljhaveri)
[![GitHub](https://img.shields.io/badge/GitHub-Explore-black?logo=github)](https://github.com/KBJ19)
[![Email](https://img.shields.io/badge/Email-Write-informational?logo=gmail)](mailto:khushalbjhaveri@gmail.com)
""")
