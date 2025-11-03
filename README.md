# AI Image Caption Generator

An AI-powered web app that describes any image using a pretrained **BLIP (Vision-Language) model**.
Built in Python with **PyTorch**, **Transformers**, and **Streamlit**.

---

## 🚀 Features

- Upload any image or use drag-and-drop
- GPU-accelerated inference (CUDA supported)
- Adjustable **creativity (temperature)** and decoding parameters
- Clean Streamlit interface
- Ready for extension (translation, FastAPI backend, React UI)

---

## 🧩 Tech Stack

- **Python 3.13**
- **PyTorch + CUDA**
- **Hugging Face Transformers**
- **Streamlit**

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/<yourusername>/AI-Image-Caption-Generator.git
cd AI-Image-Caption-Generator
```

### 2. Create & activate a virtual environment

```bash
py -3.13 -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app_streamlit.py
```

Then open the link in your browser (usually http://localhost:8501).

---

## 🧠 How It Works

1. The BLIP model encodes the image (Vision Transformer)
2. A text decoder predicts one word at a time to describe the image
3. You control randomness via the temperature slider
