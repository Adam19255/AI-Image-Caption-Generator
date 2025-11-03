# 🧠 AI Image Caption Generator

An **AI-powered local app** that generates human-like descriptions for images using a **Vision + Language** model (BLIP).  
This project was built as part of my mission to **understand how AI models connect visual perception and natural language**.

---

## 🎯 Goals & Learning Outcomes

This project was designed to help me learn:

- How **Computer Vision (ViT)** and **Natural Language Processing (GPT)** combine into multimodal AI
- How to perform **inference** efficiently on GPU (CUDA)
- How to control model **generation parameters** like `temperature`, `top_k`, and `top_p`
- How to extend a Python AI project into a **full-stack app** (FastAPI backend + React frontend)

---

## 🚀 Features

✅ Upload any image or drag & drop  
✅ Real-time caption generation using BLIP  
✅ GPU-accelerated inference (CUDA compatible)  
✅ Adjustable parameters:

- **Temperature** — controls creativity  
  ✅ FastAPI + React integration

---

## 🛠️ Setup & Run (Local Only)

### 1️⃣ Clone the repository

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

### 4. Run the FastAPI server

```bash
uvicorn server.main:app --reload
```

The API will start at http://127.0.0.1:8000

---

### Frontend Setup (React)

Open a new terminal and run:

```bash
cd frontend
npm install
npm run dev
```

The React app will start at http://localhost:5173

## 🧠 How It Works

1. The image is uploaded from the React frontend.
2. FastAPI receives the image file and passes it to the BLIP model.
3. The model encodes visual features (ViT encoder).
4. The text decoder (GPT-style) generates a caption token by token.
5. Sampling parameters (temperature) adjust the style of generation.
6. The final caption is returned to the frontend and displayed to the user.
