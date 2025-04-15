import streamlit as st

st.set_page_config(page_title="Blog | Khushal Jhaveri", layout="wide")
st.title("📝 My Blog")
st.write("Reflections, breakdowns, and build stories from my favorite AI and systems projects.")

# Blog 1
st.header("🧠 Summarizing YouTube with AI: Building a Transcript Summarizer")
st.caption("📅 14 Apr, 2025")
st.markdown("""
YouTube videos are treasure troves of knowledge, but finding key insights can be a hassle. So, I built a tool to auto-summarize YouTube content.

I used `youtube-transcript-api` to extract transcripts, then chunked them using **semantic overlap** and **sentence segmentation**.
Each chunk was passed through an **OpenAI GPT** model with custom prompts to generate summaries.

**The result:** A TL;DR interface inside a Streamlit app. Paste a link, get a digest.

**What I learned:**
- Prompt design matters more than you think.
- Chunking logic affects factuality.
- UX-first tools get shared more.

**Stack:** OpenAI API, NLTK, Streamlit, Python
""")

st.markdown("---")

# Blog 2
st.header("🎨 Visualizing Sorting Algorithms with AI: Using Vision and GANs")
st.caption("📅 14 Apr, 2025")
st.markdown("""
Not all AI needs to be utility-driven — some projects are just about beauty in logic.

Here, I visualized sorting algorithms using a **GAN-inspired morphing technique**. Shapes transitioned visually with each step of the algorithm:
- **Bubble sort**: slow swelling and sliding.
- **Quicksort**: sharp splitting and merging.

The goal wasn’t to teach sorting — it was to **feel** it. And it made me love the artistry hidden in computation.

**What I learned:**
- GANs can be used creatively without full pipelines.
- Algorithmic motion has unique visual patterns.
- Making things delightful > just functional.

**Stack:** PyTorch, GAN-style interpolations, matplotlib animations
""")

st.markdown("---")

# Blog 3
st.header("🤟 Sign Language to Text using AI: Real-Time Gesture Recognition")
st.caption("📅 14 Apr, 2025")
st.markdown("""
Communication should be inclusive. That’s why I worked on a prototype that converts **ASL signs to text** using vision-based AI.

Using **MediaPipe Hands** for landmark detection and a lightweight **MLP classifier**, the system could identify fingerspelling signs in real-time from webcam input.

**What made it fun:**
- Hands vary *a lot*. Generalization was hard.
- Latency vs accuracy was a constant tradeoff.
- Made me appreciate gesture learning in embodied AI.

**Stack:** MediaPipe, OpenCV, PyTorch, Streamlit, NumPy
""")

st.markdown("---")

# Blog 4
st.header("📟 Detecting Gallbladder Stones with AI: A Deep Learning Ultrasound Project")
st.caption("📅 14 Apr, 2025")
st.markdown("""
I wanted to try AI for medical imaging, but with a focus on **low-resource settings**.

Built a CNN that classifies gallbladder stones from **low-res ultrasound scans**. The real challenge?
- **Data quality** was noisy.
- Needed **OpenCV** tricks for noise reduction, contrast adjustment.
- Used **Grad-CAM** for interpretability — docs love seeing *why* it predicted what it did.

**What I learned:**
- Real-world deployment = robustness first.
- Simplicity + preprocessing > complex models on raw data.

**Stack:** TensorFlow, OpenCV, Grad-CAM
""")

st.markdown("---")

# Blog 5
st.header("📦 How I Used TF-IDF, Word2Vec, and MLPs to Analyze Job Descriptions")
st.caption("📅 14 Apr, 2025")
st.markdown("""
I once scraped hundreds of tech job listings to find what skills were truly in demand.

The idea was to analyze the **frequency, co-occurrence**, and **semantic similarity** of terms across postings.
- Used **TF-IDF** to rank keywords.
- Mapped similar roles using **Word2Vec** trained on the corpus.
- Built a **MLP classifier** to group descriptions by job category.

**What stood out:**
- Buzzwords ≠ core skills.
- NLP on unstructured HR text needs a lot of cleaning.
- Word2Vec + cosine scores = great for clustering.

**Stack:** Scikit-learn, Gensim, Python, matplotlib
""")

st.markdown("---")

st.success("More blogs coming soon — follow me on [LinkedIn](https://linkedin.com/in/khushaljhaveri) for updates!")
