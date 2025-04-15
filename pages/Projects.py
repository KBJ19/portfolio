import streamlit as st
st.title("🛠 Projects")
st.write("""
Here's a curated collection of my most meaningful projects — where I combined AI, vision, and language to build tools that work in the real world. Some are academic, others from internships or hackathons — but all of them taught me something valuable.
""")

# Multimodal Emotion Recognition
with st.container():
    st.subheader("🧠 Multimodal Emotion Recognition")
    st.markdown("""
    Using the **MELD** dataset, I built an emotion classifier combining:
    - **Facial expressions** via **MediaPipe + ResNet**
    - **Audio tone** with **Librosa features**
    - **Text transcripts** using **TF-IDF** and **Word2Vec**
    Fused these into a single feature space and trained a **bi-directional LSTM**.
    
    Achieved ~74% accuracy. One of my favorite deep dives into multimodal learning.
    """)
    st.caption("Tags: #DeepLearning #Multimodal #LSTM #NLP #ComputerVision")

# Gallbladder Stone Detection
with st.expander("📟 Gallbladder Stone Detection (Ultrasound)"):
    st.markdown("""
    Built a CNN-based classifier for noisy ultrasound images to identify gallbladder stones. Trained on low-resolution scans using **TensorFlow**, with heavy **OpenCV preprocessing** (contrast + noise filtering).

    Designed for low-cost deployment in rural medical settings.
    """)
    st.caption("Tags: #MedicalImaging #TensorFlow #CNN #OpenCV")

# YouTube Transcript Summarizer
with st.expander("📽️ YouTube Transcript Summarizer"):
    st.markdown("""
    Pulled video transcripts using `youtube-transcript-api`, semantically chunked them, and used **OpenAI's GPT model** with tuned prompts to generate summaries.

    Integrated into a lightweight Streamlit frontend for one-click summarization.
    """)
    st.caption("Tags: #LLM #Summarization #PromptEngineering #Streamlit")

# Amazon Sentiment Classifier
with st.expander("🛒 Amazon Review Sentiment Classifier"):
    st.markdown("""
    Worked on a custom **LSTM with attention layers** trained on Amazon review data. 
    
    Included full NLP pipeline: stopword removal, tokenization, GloVe embedding matrix.
    """)
    st.caption("Tags: #SentimentAnalysis #LSTM #NLP #Attention")

# Vocabulary Generator
with st.expander("🧾 Vocabulary Generator"):
    st.markdown("""
    A creative tool that takes in a word and generates contextually related advanced vocabulary.
    
    Built with custom word embeddings and a fine-tuned generator layer on top.
    """)
    st.caption("Tags: #NLP #Embedding #Creativity")

# GAN Sorting Visualizer
with st.expander("🎨 Sorting Visualizer with GANs"):
    st.markdown("""
    Created a GAN-based animation that visualizes sorting algorithms using 2D shape morphing. A fun intersection of algorithm visualization and generative art.
    """)
    st.caption("Tags: #GAN #Visualization #Algorithms #CreativeAI")

st.markdown("---")
st.info("Want to dive deeper into any of these? Just reach out or check the GitHub repo for code and writeups.")
