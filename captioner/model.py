"""
This module loads and initializes the image captioning model (BLIP).
It handles:
- Selecting the correct device (GPU/CPU)
- Loading the pretrained model and processor from Hugging Face
- Providing access to them for inference
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Choose the best device automatically
device = "cuda" if torch.cuda.is_available() else "cpu"

# Model ID from Hugging Face
MODEL_ID = "Salesforce/blip-image-captioning-base"

# Load processor (handles image preprocessing & text decoding)
processor = BlipProcessor.from_pretrained(MODEL_ID)

# Load the model itself
# to(device) moves it to the GPU for faster inference
model = BlipForConditionalGeneration.from_pretrained(MODEL_ID).to(device)

# Set model to evaluation mode (important for inference only)
model.eval()

# Export these variables so other files can import them
__all__ = ["model", "processor", "device"]
