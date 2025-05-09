import streamlit as st
from PIL import Image

st.set_page_config(page_title="Blog | Khushal Jhaveri", layout="wide")

st.title("📝 Blog")

st.write("""
Here’s a curated collection of my technical blog posts — deep dives into projects that blend AI, vision, and language. These posts aren’t just code walkthroughs, but narratives about how each project unfolded, what I learned, and how I tackled the unexpected. Grab a coffee and take a scroll. ☕️
""")

st.markdown("---")

blog_posts = [
    {
        "emoji": "🎭",
        "title": "Multimodal Emotion Recognition System Using BERT, HuBERT, EfficientNet, and Fusion Techniques",
        "url": "https://building-an-ai-that-understands-emotions.hashnode.dev/how-i-built-a-multimodal-emotion-recognition-system-using-bert-hubert-efficientnet-and-fusion-techniques"
    },
    {
        "emoji": "📦",
        "title": "How I Used TF-IDF, Word2Vec, and MLPs to Analyze Sentiment in Amazon Reviews",
        "url": "https://building-an-ai-that-understands-emotions.hashnode.dev/how-i-used-tf-idf-word2vec-and-mlps-to-analyze-sentiment-in-amazon-reviews"
    },
    {
        "emoji": "📺",
        "title": "Summarizing YouTube with AI: Building a Transcript-to-Insight Tool Using LLMs",
        "url": "https://building-an-ai-that-understands-emotions.hashnode.dev/summarizing-youtube-with-ai-building-a-transcript-to-insight-tool-using-llms"
    },
    {
        "emoji": "🩺",
        "title": "Detecting Gallbladder Stones with AI: A Deep Learning Approach Using Ultrasound",
        "url": "https://building-an-ai-that-understands-emotions.hashnode.dev/detecting-gallbladder-stones-with-ai-a-deep-learning-approach-using-ultrasound"
    },
    {
        "emoji": "🤟",
        "title": "Sign Language to Text using AI: Real-Time Gesture Recognition with MediaPipe and LSTMs",
        "url": "https://building-an-ai-that-understands-emotions.hashnode.dev/sign-language-to-text-using-ai-real-time-gesture-recognition-with-mediapipe-and-lstms"
    },
    {
        "emoji": "🔁",
        "title": "Visualizing Sorting Algorithms with AI: Using Vision Transformers and GANs to Teach Logic",
        "url": "https://building-an-ai-that-understands-emotions.hashnode.dev/visualizing-sorting-algorithms-with-ai-using-vision-transformers-and-gans-to-teach-logic"
    },
]

for post in blog_posts:
    st.markdown(f"#### {post['emoji']} [**{post['title']}**]({post['url']})")

st.markdown("---")
st.info("More posts coming soon! If there's something you'd like me to write about — feel free to reach out via the Contact page.")
