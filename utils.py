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
- Designed a system that combines facial expressions (video via MediaPipe + ResNet), tone (Librosa on audio), and transcripts (TF-IDF, Word2Vec on text) to classify human emotions.
- Dataset used: MELD.
- Achieved ~74% accuracy using early fusion of features and LSTM classifier.

2. Gallbladder Stone Detection using Ultrasound:
- Built a CNN-based classifier to detect presence of stones in low-resolution, noisy ultrasound images.
- Tools used: TensorFlow, OpenCV, Keras.
- Focused on preprocessing for contrast enhancement and edge detection.
- Designed for deployment in low-resource medical settings.

3. YouTube Transcript Summarizer:
- Created an LLM-powered tool that extracts video transcripts and generates context-aware summaries using OpenAI API.
- Integrated streamlit UI and included semantic chunking + chain-of-thought prompts.

4. Amazon Product Review Sentiment Classifier:
- Built an LSTM model to classify reviews into sentiment categories using glove embeddings and attention layers.
- Implemented preprocessing: tokenization, stopword removal, lemmatization.
- Dataset: public Amazon reviews.

5. Vocabulary Generator:
- Given a keyword or concept, the app generates a list of related advanced vocabulary using word embeddings + a finetuned text generator.
- Goal: aid competitive exam takers or writers.

6. Sorting Algorithm Visualizer with GANs:
- Visualizes sorting algorithms using 2D shape transformations.
- Uses StyleGAN to generate shapes and overlays sorting steps dynamically.
- Adds an educational visual layer to classic algorithm understanding.

Skills:
- Python, TensorFlow, PyTorch, OpenCV, Streamlit, YOLOv8, HuggingFace Transformers, MediaPipe, LLM prompt engineering, NLP pipelines

Respond as Khushal’s AI assistant using only the context above.
    """

    prompt = f"{context.strip()}\n\nUser: {query}\nKhushal’s AI Assistant:"

    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xl"
    headers = {
        "Authorization": f"Bearer {st.secrets['huggingface']['HF_TOKEN']}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 300,
            "do_sample": False
        },
        "options": {
            "wait_for_model": True
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].replace(prompt, "").strip()
        elif "error" in result:
            return f"⚠️ Model error: {result['error']}"
        else:
            return f"⚠️ Unexpected model response: {result}"
    except Exception as e:
        return f"❌ Error: {e}"
