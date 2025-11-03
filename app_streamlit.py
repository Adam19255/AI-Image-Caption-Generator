"""
Streamlit interface for the AI Image Caption Generator.
Run:
    streamlit run app_streamlit.py
Then open the link shown in the terminal (usually http://localhost:8501)
"""

import streamlit as st
from captioner.inference import generate_caption
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="AI Image Caption Generator", page_icon="🧠")

# Page header
st.title("🧠 AI Image Caption Generator")
st.write("Upload an image and let the AI describe it. Adjust the *Creativity* slider to control randomness.")

# --- Sidebar controls ---
st.sidebar.header("⚙️ Settings")
temperature = st.sidebar.slider(
    "Creativity (temperature)",
    min_value=0.1,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Lower = more factual, Higher = more creative"
)
top_k = st.sidebar.slider("Top-K", 0, 100, 50, 5)
top_p = st.sidebar.slider("Top-P (nucleus sampling)", 0.1, 1.0, 0.9, 0.05)

# --- Image uploader ---
uploaded_image = st.file_uploader("📸 Upload an image", type=["jpg", "jpeg", "png"])

# --- Display and caption ---
if uploaded_image is not None:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("✨ Generate Caption"):
        with st.spinner("AI is thinking..."):
            caption = generate_caption(
                image_input=image,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p
            )
        st.success("**Caption:** " + caption)
