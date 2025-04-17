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
