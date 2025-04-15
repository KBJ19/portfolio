import streamlit as st
from PIL import Image

st.set_page_config(page_title="About | Khushal Jhaveri", layout="wide")

# Layout: Profile image on left, content on right
col1, col2 = st.columns([1, 3], gap="large")
with col1:
    image = Image.open("assets/profile-pic (3).png")
    st.image(image, caption="Khushal Jhaveri", width=200)

with col2:
    st.title("👋 About Me")
    st.write("""
Hi, I'm **Khushal Jhaveri** — currently pursuing my Master’s in Computer Science with a focus on Artificial Intelligence at the **University of Southern California (USC)**.

I like building systems that sit at the intersection of **AI, vision, and language** — things that make machines understand humans a little better, and maybe even help out in the real world.

Over the past few years, I’ve worked on everything from **multimodal emotion recognition**, to **drone vision systems**, to **textbook readability tools** for underserved communities — always aiming for impact over just accuracy.

Before USC, I studied at **K.J. Somaiya College in Mumbai**, led as **Marketing Head at BloomBox**, and worked on cybersecurity honors coursework.

I’ve interned as a **Deep Learning Engineer at ResoluteAI** and as a **Machine Learning Intern at Suvidha Foundation**, applying computer vision where it actually helps people.
""")

st.markdown("---")

st.header("💬 Outside the Resume")
st.write("""
I’m an extrovert who loves chaos and deep dives — from hosting 1000+ attendee startup events to debugging code at 3am. I think tech is at its best when it connects people, solves things quietly, and makes someone's day better.
""")

st.markdown("---")

st.header("☕ Interests Outside Tech")
st.write("""
- 🍜 **Foodie** — From street snacks to slow cooking, always exploring flavor.
- 📸 **Photography** — Candid moments, cityscapes, and clouds.
- 🚴‍♂️ **Cycling** — Long rides = deep thinking time.
- 🥋 **Martial Arts** — Focus, movement, clarity.
- 🚗 **Cars** — All things that move, roar, or roll.
""")

st.markdown("---")

st.header("🧠 What Drives Me")
st.write("""
I don’t chase the fanciest model — I look for the **right one**. I love building fast, failing smart, and creating things that work in the wild. If I can share that with others through mentoring, open source, or just vibing over shared ideas — all the better.

Thanks for stopping by. Feel free to connect!
""")

st.markdown("---")

# Social links
st.subheader("📬 Let's Connect")
st.markdown("""
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](http://www.linkedin.com/in/khushaljhaveri)
[![GitHub](https://img.shields.io/badge/GitHub-Explore-black?logo=github)](https://github.com/KBJ19)
[![Email](https://img.shields.io/badge/Email-Write-informational?logo=gmail)](mailto:khushalbjhaveri@gmail.com)
""")
