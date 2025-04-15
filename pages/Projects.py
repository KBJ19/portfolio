import streamlit as st

st.set_page_config(page_title="Projects | Khushal Jhaveri", layout="wide")

st.title("🛠 Projects")
st.write("""
Here’s a curated showcase of the projects I’ve built — where AI, vision, and language come together to solve meaningful problems. Each one taught me something new, and most importantly, brought me closer to building systems that work beyond just labs.
""")

# Multimodal Emotion Recognition
with st.container():
    st.subheader("🧠 Multimodal Emotion Recognition")
    st.markdown("""
    One of my most fulfilling projects — building a system that can understand **how people feel** by analyzing not just what they say, but *how* they say it and *how* they look while saying it.

    Using the **MELD** dataset (multi-modal emotion dialogues from Friends), I extracted:
    - **Facial features** using **MediaPipe** + downsampled **ResNet embeddings**
    - **Audio tone** using **Librosa** features like chroma, MFCCs, and spectral contrast
    - **Transcript embeddings** using both **TF-IDF** and pre-trained **Word2Vec**
    
    I aligned these at the utterance level, fused them via early fusion, and trained a **bi-directional LSTM** to classify emotion.

    The result? A ~74% test accuracy on a 7-class emotion set — and a deeper appreciation for **multimodal alignment** and **temporal feature fusion**.
    """)
    st.caption("Tags: #DeepLearning #Multimodal #LSTM #NLP #ComputerVision")

# Gallbladder Stone Detection
with st.expander("📟 Gallbladder Stone Detection (Ultrasound)"):
    st.markdown("""
    Built a lightweight CNN classifier for **diagnosing gallbladder stones** from noisy, low-resolution ultrasound images — aimed at **rural medical settings** where specialists are scarce.

    - Used **OpenCV** to enhance scan clarity via histogram equalization, bilateral filtering, and threshold-based segmentation
    - Developed a **custom TensorFlow CNN** with low parameter count to fit low-power devices
    - Integrated interpretability via **Grad-CAM** to highlight possible stone regions

    This was a great blend of medical imaging, classical preprocessing, and responsible model design for accessibility.
    """)
    st.caption("Tags: #MedicalImaging #TensorFlow #CNN #OpenCV")

# YouTube Transcript Summarizer
with st.expander("📽️ YouTube Transcript Summarizer"):
    st.markdown("""
    Ever wanted to **get the gist of a 30-minute talk** in 30 seconds? I built this tool for exactly that.

    - Extracts subtitles using `youtube-transcript-api`
    - Breaks them into coherent semantic chunks using sliding context windows
    - Feeds them into **OpenAI GPT** with tuned prompts for summarization
    - Outputs section-wise summaries that retain nuance

    Wrapped the entire workflow in a Streamlit UI. I used this tool myself to summarize AI lectures and keynotes.
    """)
    st.caption("Tags: #LLM #Summarization #PromptEngineering #Streamlit")

# Amazon Sentiment Classifier
with st.expander("🛒 Amazon Review Sentiment Classifier"):
    st.markdown("""
    A full-fledged sentiment analysis pipeline that classifies product reviews as **positive**, **neutral**, or **negative** — using an **LSTM with attention**.

    - Cleaned review text (punctuation, stopwords, lemmatization)
    - Tokenized and embedded with **GloVe**
    - Trained a deep **LSTM** followed by attention mechanism for long-range dependency handling

    This project made me comfortable with **sequence modeling**, **imbalanced dataset handling**, and tuning **loss functions** (e.g. focal loss for rare sentiments).
    """)
    st.caption("Tags: #SentimentAnalysis #LSTM #Attention #NLP")

# Vocabulary Generator
with st.expander("🧾 Vocabulary Generator"):
    st.markdown("""
    I built this project for students like me who wanted to expand their vocab — **without relying on static word lists**.

    - Takes a seed word (e.g. “happy”) and returns semantically related **advanced vocabulary** (e.g. “elated”, “jubilant”, “exuberant”)
    - Powered by custom **Word2Vec + FastText** ensemble embeddings
    - Fine-tuned generator with semantic similarity scoring

    The goal was **creative utility** — helping users write better essays, stories, or social media posts.
    """)
    st.caption("Tags: #NLP #Embeddings #WordPlay #Education")

# GAN Sorting Visualizer
with st.expander("🎨 Sorting Visualizer with GANs"):
    st.markdown("""
    What if sorting algorithms looked more like **animated shape transformations**?

    - I used a **StyleGAN-inspired setup** to create smooth transitions between 2D shapes representing array states during sorting (bubble, quick, merge, etc.)
    - The visuals morph between states based on algorithmic steps

    It was a crazy blend of **generative models** + **algorithmic education**, and I loved every bit of it. One of the most *fun* projects I’ve built.
    """)
    st.caption("Tags: #GAN #CreativeAI #Visualization #Algorithms")

st.markdown("---")
st.info("Each of these taught me more than just code — they taught me how to design, debug, communicate, and keep building. Want to collaborate on something similar? Let’s talk.")
