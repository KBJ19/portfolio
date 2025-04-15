import streamlit as st

st.set_page_config(page_title="Projects | Khushal Jhaveri", layout="wide")

st.title("🛠 Projects")
st.write("""
Here’s a curated showcase of the projects I’ve built — where AI, vision, and language come together to solve meaningful problems. Each one taught me something new, and most importantly, brought me closer to building systems that work beyond just labs.
""")

# Multimodal Emotion Recognition
with st.expander("🧠 Multimodal Emotion Recognition"):
    st.markdown("""
One of my most fulfilling projects — building a system that can understand **how people feel** by analyzing not just what they say, but *how* they say it and *how* they look while saying it.

Using the **MELD** dataset (multi-modal emotion dialogues from *Friends*), I extracted:
- **Facial features** using **MediaPipe** for landmark extraction and downsampled **ResNet** for visual embeddings
- **Audio tone** using **Librosa** features like chroma, MFCCs, zero-crossing rate, and spectral contrast
- **Transcript embeddings** using both **TF-IDF** and pre-trained **Word2Vec**

I aligned these three modalities at the utterance level, fused them using **early fusion**, and trained a **bi-directional LSTM** to classify emotions. This also included dropout regularization, gradient clipping, and class-balancing to handle underrepresented emotions.

Achieved ~74% test accuracy across 7 emotion classes. More than the accuracy, this project taught me the nuances of **temporal alignment**, **feature fusion**, and how to design models that feel more *emotionally aware*.
""")
    st.caption("Tags: #DeepLearning #Multimodal #LSTM #NLP #ComputerVision")

# Gallbladder Stone Detection
with st.expander("📟 Gallbladder Stone Detection (Ultrasound)"):
    st.markdown("""
Built a lightweight CNN classifier for **diagnosing gallbladder stones** from noisy, low-resolution ultrasound images — aimed at **rural medical settings** where specialists are scarce.

- Used **OpenCV** to enhance scan clarity via histogram equalization, bilateral filtering, and contour thresholding
- Trained a custom **TensorFlow CNN** architecture to work on edge devices
- Implemented **Grad-CAM** visualizations to highlight detected regions for interpretability

This was my first attempt at responsible AI for healthcare — balancing performance with accessibility.
""")
    st.caption("Tags: #MedicalImaging #TensorFlow #CNN #OpenCV")

# YouTube Transcript Summarizer
with st.expander("📽️ YouTube Transcript Summarizer"):
    st.markdown("""
A tool to help you get the **key takeaways from long videos**, fast.

- Extracted subtitles using `youtube-transcript-api`
- Cleaned and chunked them semantically using sliding window + cosine similarity
- Fed chunks to **OpenAI's GPT API** with tailored summarization prompts
- Integrated into a **Streamlit frontend** for real-time use

This project taught me prompt engineering, semantic coherence, and usability design — and I still use it myself.
""")
    st.caption("Tags: #LLM #Summarization #PromptEngineering #Streamlit")

# Amazon Sentiment Classifier
with st.expander("🛒 Amazon Review Sentiment Classifier"):
    st.markdown("""
Built a full NLP pipeline to classify Amazon reviews into **positive**, **neutral**, or **negative** using:

- **Text cleaning**: punctuation stripping, lemmatization, lowercasing
- **Embedding layer** using pre-trained **GloVe vectors**
- **LSTM with attention layer** for long-term dependencies
- Trained using weighted cross-entropy loss to handle class imbalance

This gave me hands-on practice with sequence modeling, custom attention blocks, and evaluation beyond accuracy (precision, F1).
""")
    st.caption("Tags: #SentimentAnalysis #LSTM #Attention #NLP")

# Vocabulary Generator
with st.expander("🧾 Vocabulary Generator"):
    st.markdown("""
A creative NLP project that helps users find **high-impact vocabulary** starting from a seed word.

- Merged **Word2Vec** and **FastText** vectors to build a richer semantic neighborhood
- Trained a shallow transformer head to **generate synonyms** ranked by semantic weight and register
- Designed the UI to be playful — great for essay writers, content creators, or curious learners

This one pushed me to think beyond tech: about language, nuance, and user delight.
""")
    st.caption("Tags: #NLP #Embeddings #WordPlay #SemanticSearch")

# GAN Sorting Visualizer
with st.expander("🎨 Sorting Visualizer with GANs"):
    st.markdown("""
An artistic project where I re-imagined how we teach **sorting algorithms** — not with bars, but with **morphing geometric shapes**.

- Used **StyleGAN-inspired generator** to animate state transitions in arrays
- Encoded bubble sort, merge sort, and quick sort into morphing flows
- Created a small GUI where students could visualize sort evolution in a *fluid*, *visual* way

Purely for fun and curiosity, but got great feedback from peers learning algorithms.
""")
    st.caption("Tags: #GAN #CreativeAI #Visualization #Algorithms")

st.markdown("---")
st.info("Each of these taught me more than just code — they taught me how to design, debug, communicate, and keep building. Want to know more about these, check out my github or Linkedln Profile")
