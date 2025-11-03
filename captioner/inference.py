"""
This module defines functions to generate captions from images
using the pretrained BLIP model (loaded in model.py).

It focuses on the *inference* process:
- preprocessing the image
- running the model to generate text
- postprocessing (decoding) the output
"""

from captioner.model import model, processor, device
from captioner.utils import load_image
import torch

@torch.inference_mode()
def generate_caption(
    image_input,
    temperature: float = 1.0,
    top_k: int = 50,
    top_p: float = 0.9,
    max_new_tokens: int = 50
) -> str:
    """
    Generate a text caption for a given image.

    Args:
        image_input: Can be a local path, URL, or a PIL.Image object.
        temperature (float): Controls randomness (1.0 = balanced).
        top_k (int): Keep only the top K most likely next words.
        top_p (float): Nucleus sampling cutoff (0.9 = keep 90% most likely words).
        max_new_tokens (int): Max words/tokens to generate.

    Returns:
        str: The generated caption text.
    """

    # Step 1 — Load and preprocess the image
    image = load_image(image_input)
    inputs = processor(image, return_tensors="pt").to(device)

    # Step 2 — Generate caption using the model
    output_ids = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        do_sample=True  # enables randomness for temperature/top_k/top_p
    )

    # Step 3 — Decode the output tokens into human-readable text
    caption = processor.decode(output_ids[0], skip_special_tokens=True)

    return caption.strip()
