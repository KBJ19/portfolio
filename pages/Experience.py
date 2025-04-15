import streamlit as st

st.set_page_config(page_title="Experience | Khushal Jhaveri", layout="wide")

st.title("💼 Experience")
st.write("""
Here’s a quick look at some of the roles where I’ve applied my skills in real-world settings — from AI in agriculture and education to running events with thousands of people.

Every experience taught me something different: how to solve problems, how to work with people, and how to keep learning on the job.
""")

# ResoluteAI
with st.container():
    st.subheader("🧠 Deep Learning Intern — ResoluteAI")
    st.caption("Mumbai, India · Summer 2023")
    st.markdown("""
At ResoluteAI, I worked on AI-powered drone vision systems for agriculture and infrastructure.

- Designed custom **YOLOv8-based pipelines** to detect defective infrastructure and irrigation leaks in aerial footage
- Built a **sapling counter** for agriculture clients using OpenCV + YOLO — achieved over 95% accuracy
- Developed a Streamlit dashboard to visualize inference results for client-facing demo day

This internship gave me a real appreciation for performance-vs-accuracy tradeoffs, edge deployment challenges, and what it means to build something useful in the wild.
""")

# Suvidha Foundation
with st.container():
    st.subheader("📚 Machine Learning Intern — Suvidha Foundation")
    st.caption("Remote · Spring 2023")
    st.markdown("""
At Suvidha Foundation, I contributed to an edtech outreach initiative focused on improving access to quality education for rural girls.

- Preprocessed **mobile-scanned textbook images** using OpenCV: adaptive thresholding, denoising, and morphological cleaning
- Improved readability and contrast of low-resolution learning material distributed to over 100 students
- Supported outreach and crowdfunding campaigns for distributing tech-driven learning kits

This was a reminder that even simple models and classic computer vision can have real impact.
""")

# BloomBox
with st.container():
    st.subheader("📣 Marketing Head — BloomBox, Entrepreneurship Cell")
    st.caption("K.J. Somaiya College · 2021–2022")
    st.markdown("""
At BloomBox, I wasn’t just organizing events — I was helping run a full-fledged student startup incubator.

- Led sponsorship outreach and closed deals that funded **70% of our flagship summit**
- Managed end-to-end execution for **a 1000+ attendee event** with **Ashneer Grover** as the keynote speaker
- Built all pitch decks, emails, and handled content + marketing strategy

This taught me how to write, how to pitch, and how to make things happen even with messy resources and tighter timelines.
""")

st.markdown("---")
st.info("More experiences available on my resume — feel free to reach out if you’d like to talk about any of these or grab a copy!")
