import requests
import streamlit as st

def generate_response(query):
    context = """
Khushal Jhaveri is a Master’s student in Computer Science at the University of Southern California (USC), with a specialization in Artificial Intelligence. He is deeply passionate about building real-world systems at the intersection of AI, vision, and language.

Internships:

1. Deep Learning Intern at ResoluteAI:
- Worked on drone vision systems for agriculture and infrastructure inspection.
- Built YOLOv8-based detection pipelines to identify defective sections in infrastructure footage.
- Created a sapling counter using OpenCV and YOLOv8 that achieved 95%+ accuracy.
- Designed a Streamlit dashboard for visual inspection tasks and data overlay.

2. Machine Learning Intern at Suvidha Foundation:
- Improved readability of blurry mobile-scanned textbooks for underprivileged girls.
- Applied OpenCV-based image preprocessing: contrast stretching, adaptive thresholding, morphological ops.
- Output was used in educational kits for over 100 girls in rural regions.
- Assisted in outreach campaigns and fundraising for NGO causes.

3. Marketing Head at BloomBox:
- Led marketing strategy, growth, and campaign execution for the student-run startup cell.
- Organized a 1000+ attendee event with Ashneer Grover as keynote speaker.
- Built sponsorship pitch decks and secured 70% of event funding from cold email outreach.
- Led a team of 8 volunteers for end-to-end event operations.

Projects:

1. Multimodal Emotion Recognition:
- Combined facial expressions (via MediaPipe + ResNet), tone (Librosa on audio), and transcripts (TF-IDF, Word2Vec on text) to classify emotions.
- Dataset used: MELD. Achieved ~74% accuracy using early fusion of features and LSTM.

2. Gallbladder Stone Detection using Ultrasound:
- Built a CNN-based classifier for noisy ultrasound images using TensorFlow and OpenCV.
- Designed for deployment in low-resource medical settings.

3. YouTube Transcript Summarizer:
- Used OpenAI GPT and prompt engineering to summarize YouTube transcripts.
- Integrated with Streamlit and semantic chunking.

4. Amazon Product Review Sentiment Classifier:
- Used LSTM + attention layers on public Amazon reviews.
- Applied stopword removal, tokenization, and glove embeddings.

5. Vocabulary Generator:
- Generates related advanced vocabulary using embedding lookups + a fine-tuned generator model.

6. Sorting Visualizer with GANs:
- StyleGAN-based visualization of sorting algorithms over 2D shape transformations.

Skills:
- Python, TensorFlow, PyTorch, OpenCV, Streamlit, YOLOv8, HuggingFace Transformers, MediaPipe, LLM prompt engineering, NLP pipelines
"""

    prompt = f"""Below is background information about Khushal Jhaveri. Use this information only to answer the user's question.

### CONTEXT:
{context.strip()}

### QUESTION:
{query}

### ANSWER:
"""

    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {
        "Authorization": f"Bearer {st.secrets['huggingface']['HF_TOKEN']}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 400,
            "temperature": 0.7,
            "do_sample": False
        },
        "options": {"wait_for_model": True}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
        elif "error" in result:
            return f"⚠️ Model error: {result['error']}"
        else:
            return f"⚠️ Unexpected model response: {result}"
    except Exception as e:
        return f"❌ Error: {e}"
