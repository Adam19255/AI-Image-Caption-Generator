"""
Utility functions for the captioning project.
Handles:
- Loading images from local paths or URLs
- Converting them to the correct RGB format
- Basic error handling
"""

from PIL import Image
import requests
from io import BytesIO
import os

def load_image(image_input):
    """
    Loads an image from a file path, URL, or directly from a PIL.Image object.

    Args:
        image_input: str | PIL.Image.Image
            - A local file path (e.g. "photo.jpg")
            - A URL (e.g. "https://picsum.photos/500")
            - A PIL.Image object (already loaded)

    Returns:
        PIL.Image.Image object in RGB mode.
    """
    # Case 1 — already a PIL image (user passed it directly)
    if isinstance(image_input, Image.Image):
        image = image_input

    # Case 2 — input is a URL (starts with http or https)
    elif isinstance(image_input, str) and image_input.startswith(("http://", "https://")):
        try:
            response = requests.get(image_input, stream=True, timeout=10)
            response.raise_for_status()  # raise an error for 404/403
            image = Image.open(BytesIO(response.content))
        except Exception as e:
            raise ValueError(f"Could not download image from URL: {e}")

    # Case 3 — input is a local file
    elif isinstance(image_input, str) and os.path.exists(image_input):
        try:
            image = Image.open(image_input)
        except Exception as e:
            raise ValueError(f"Could not open local image: {e}")

    else:
        raise ValueError("Invalid image input. Must be a path, URL, or PIL.Image object.")

    # Always convert to RGB (BLIP expects 3 color channels)
    if image.mode != "RGB":
        image = image.convert("RGB")

    return image
