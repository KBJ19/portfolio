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
- **Visual input**: I used **MediaPipe** to extract facial landmarks from each video frame and passed them through a ResNet-based encoder to capture micro-expressions.
- **Audio features**: With **Librosa**, I extracted MFCCs, zero-crossing rates, and pitch contours to detect tone shifts and emotional vocal patterns.
- **Textual content**: Processed transcripts using **TF-IDF** and **Word2Vec** embeddings to encode semantic meaning.

These streams were aligned frame-by-frame and fused using early fusion before passing them into a **bi-directional LSTM**, which captured temporal dependencies across the modalities. The final classification yielded ~74% accuracy, outperforming unimodal baselines significantly.

This wasn’t just a deep learning experiment — it was about bridging the gap between cold code and human feeling. It made me appreciate the nuances in multimodal fusion and the art of aligning signals that speak different languages.
""")
    st.caption("Tags: #MultimodalAI #EmotionRecognition #LSTM #MELD #MediaPipe #ResNet #AudioTextVision")

# Gallbladder Stone Detection
with st.expander("📟 Gallbladder Stone Detection (Ultrasound)"):
    st.markdown("""
This project focused on improving the accuracy and accessibility of gallbladder stone detection using deep learning. Traditional ultrasound scans can be noisy, and diagnosis often varies by clinician. So I built a system that leverages **VGG16**, **ResNet50**, and **MobileNetV2** with **second-order pooling** to identify stones with better feature learning.

I used **region proposal networks (RPNs)** to localize the gallbladder and extracted ROIs. Preprocessing steps involved **CLAHE** contrast enhancement, contour filtering, and OpenCV pipelines to refine image input.

The model improved classification accuracy by 30% compared to standard ultrasound diagnostics and serves as a **cost-effective alternative to MRI or CT scans**, especially in resource-constrained settings.

Looking ahead, this system could be validated clinically and integrated into hospital diagnostic workflows.
""")
    st.caption("Tags: #MedicalAI #Ultrasound #CNN #RPN #CostEffectiveHealthcare")


# YouTube Transcript Summarizer
with st.expander("📽️ YouTube Transcript Summarizer"):
    st.markdown("""
We’ve all scrubbed through 45-minute videos just to find the one minute we care about. So I built a tool to skip the hunt.

The app pulls transcripts using youtube-transcript-api, breaks them into meaningful chunks based on semantic similarity, and feeds them into **OpenAI’s GPT models** with prompt engineering for summarization. Each chunk returns a short, clear summary that captures the essence of that segment.

I wrapped the whole thing in a clean **Streamlit frontend** for easy access. This was my first time integrating LLMs in a structured pipeline and reinforced how crucial **prompt design and chunking** are when working with transformer-based models.

It’s the tool I now use to study — which is the best kind of feedback loop.
""")
    st.caption("Tags: #LLM #Summarization #OpenAI #Streamlit #NLP")

# Amazon Review Sentiment Classifier
with st.expander("🛒 Amazon Review Sentiment Classifier"):
    st.markdown("""
This project involved performing **binary and ternary sentiment classification** on Amazon Office Product reviews using a combination of classic ML and deep learning approaches.

First, I carried out extensive **text cleaning** — lowercasing, lemmatization, stopword removal, HTML stripping, and punctuation filtering. I used both **pre-trained Word2Vec embeddings** and trained a **custom Word2Vec model** to encode semantic information more contextually.

For modeling, I compared:
- **Binary classifiers**: SVM, Perceptron, and MLP
- **Ternary classifiers**: MLP with 300D embeddings and reduced 10D dimensions

Findings showed that custom Word2Vec outperformed in certain domain-specific contexts, while reducing embedding dimensionality negatively impacted accuracy. My best-performing model was a **Ternary MLP with custom Word2Vec (300D)**, achieving strong classification across all sentiment classes.

Beyond just predicting sentiment, this taught me how subtle the tone of reviews can be — and how different models pick up on those cues differently.
""")
    st.caption("Tags: #SentimentAnalysis #Word2Vec #TernaryClassification #MLP #NLP")

# Sign Language
with st.expander("🧤 Sign Language to Text with MediaPipe and LSTMs"):
    st.markdown("""
One of my most rewarding explorations into AI for accessibility. I built a real-time system that converts sign language gestures into text using a webcam feed.

✔ Data Collection & Preprocessing:
- Used MediaPipe Hands API for real-time hand tracking and keypoint extraction.
- Created a dataset of various hand signs with multiple lighting conditions and angles for robustness.
- Applied Gaussian smoothing & normalization for consistent input representation.

✔ Deep Learning Model:
- **CNN (Convolutional Neural Network)**: Extracts spatial features from hand gestures.
- **LSTM (Long Short-Term Memory)**: Captures temporal dependencies in sequential hand movements.
- Trained with TensorFlow & PyTorch, optimized with Adam optimizer and learning rate decay.

✔ Results & Impact:
- Achieved 90% accuracy in real-time sign language-to-text translation.
- Improved communication efficiency by 60% for hearing-impaired individuals.
- Integrated into a user-friendly real-time interface using OpenCV for video processing.
""")
    st.caption("Tags: #SignLanguage #GestureRecognition #Accessibility #LSTM #MediaPipe")

# GAN Sorting Visualizer
with st.expander("🎨 Sorting Visualizer with GANs"):
    st.markdown("""
Sorting algorithms are often difficult to visualize and interpret.

✔ Dataset Creation:
- Generated a dataset of 250 sorting sequences (~1000+ images) representing different sorting algorithms.
- Included algorithms: QuickSort, MergeSort, BubbleSort, HeapSort.
- Labeled images with sorting states and positions to train the model.

✔ Model Selection:
- **Vision Transformers (ViTs)**: Used Self-Attention Mechanism to capture relationships between elements in a sorting sequence.
- **Conditional GANs (cGANs)**:
  - Generator: Generates sorting sequence visualizations.
  - Discriminator: Ensures the generated sequences match real sorting patterns.

✔ Results & Impact:
- Improved clarity and coherence of sorting steps by 40%.
- Attention heatmaps highlighted key regions, improving interpretability.
- Created a better educational tool for sorting algorithm learning.
""")
    st.caption("Tags: #GAN #VisionTransformers #SortingVisualization #EducationalAI")


st.markdown("---")

st.info("Each of these taught me more than just code — they taught me how to design, debug, communicate, and keep building. Want to know more about these, check out my github or Linkedln Profile")
