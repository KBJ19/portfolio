import streamlit as st

st.set_page_config(page_title="Projects | Khushal Jhaveri", layout="wide")

st.title("🛠 Projects")
st.write("""
Here’s a curated showcase of the projects I’ve built — where AI, vision, and language come together to solve meaningful problems. Each one taught me something new, and most importantly, brought me closer to building systems that work beyond just labs.
""")

# Multimodal Emotion Recognition
with st.expander("🧠 Multimodal Emotion Recognition"):
    st.markdown("""
This project came out of my curiosity about how machines can understand not just *what* people are saying, but also *how* they’re saying it — essentially, getting machines to pick up on emotion like humans do.

Using the **MELD dataset**, I built a multimodal emotion classifier that fuses three streams:
- **Visual input**: Facial landmarks via MediaPipe + ResNet.
- **Audio features**: MFCCs, ZCR, pitch (Librosa).
- **Text**: Processed with TF-IDF & Word2Vec embeddings.

I used early fusion followed by a **bi-LSTM**, achieving ~74% accuracy — outperforming unimodal setups.
""")
    st.caption("Tags: #MultimodalAI #EmotionRecognition #LSTM #MELD #MediaPipe")

# Gallbladder Stone Detection
with st.expander("📟 Gallbladder Stone Detection (Ultrasound)"):
    st.markdown("""
Improving noisy ultrasound diagnostics using deep learning. I used **ResNet, MobileNetV2, VGG16**, and **second-order pooling** to classify gallbladder stones.

Steps included:
- CLAHE + contour filtering (OpenCV)
- ROI localization with RPN
- Trained CNNs → 30% boost in diagnostic accuracy

This system provides a **cost-effective alternative** for hospitals lacking MRI/CT access.
""")
    st.caption("Tags: #MedicalAI #CNN #OpenCV #Ultrasound #Diagnostics")

# Sign Language Recognition
with st.expander("🧤 Sign Language to Text with MediaPipe and LSTMs"):
    st.markdown("""
**Problem:** Real-time sign-to-text conversion for the hearing-impaired.

✔ Data: Hand landmarks from **MediaPipe Hands**, diverse conditions  
✔ Model: **CNN-LSTM hybrid**
- CNN extracts spatial hand shape
- LSTM captures motion across frames  
✔ Tools: TensorFlow, PyTorch, OpenCV

**Results:**  
- 90% translation accuracy  
- 60% improvement in communication efficiency  
- Real-time interface using webcam stream
""")
    st.caption("Tags: #SignLanguage #GestureRecognition #CNN #LSTM #Accessibility")

# YouTube Summarizer
with st.expander("📽️ YouTube Transcript Summarizer"):
    st.markdown("""
Takes long video transcripts and returns crisp summaries using **semantic chunking + OpenAI GPT**.

Flow:
1. Pull transcript (`youtube-transcript-api`)
2. Chunk based on topic
3. Feed each into GPT with tuned prompts

Wrapped it in a clean **Streamlit UI**. Now my go-to study tool.
""")
    st.caption("Tags: #LLM #OpenAI #TranscriptSummarizer #PromptEngineering")

# Amazon Review Classifier
with st.expander("🛒 Amazon Review Sentiment Classifier"):
    st.markdown("""
Performed **binary & ternary classification** on Amazon reviews.

- Cleaned text → Word2Vec (pretrained + custom)
- Compared SVM, MLP, Perceptron
- Best model: **MLP + custom 300D Word2Vec** on ternary task

Learned how subtle review tones change outcomes across model types.
""")
    st.caption("Tags: #SentimentAnalysis #MLP #Word2Vec #TextClassification")

# GAN Sorting Visualizer
with st.expander("🎨 Sorting Visualizer with GANs"):
    st.markdown("""
**Goal:** Make sorting steps intuitive to understand through visual animation.

✔ Dataset: 1000+ frames across 250 sequences  
✔ Algorithms: QuickSort, MergeSort, HeapSort  
✔ Model:
- **Vision Transformers** for attention across steps  
- **Conditional GANs** for generating realistic sequences

**Outcome:**  
- 40% clarity boost  
- Attention maps showed where the model focused — great for teaching!
""")
    st.caption("Tags: #GAN #ViT #Sorting #Education #Visualization")

st.markdown("---")
st.info("Each of these taught me more than just code — they taught me how to design, debug, communicate, and keep building.")
