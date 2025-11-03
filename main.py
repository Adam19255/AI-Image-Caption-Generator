"""
Example usage:
    python main.py --image https://picsum.photos/400 --temperature 0.8
"""

import argparse
from captioner.inference import generate_caption

def main():
    # 1️⃣ Set up command-line argument parser
    parser = argparse.ArgumentParser(description="AI Image Caption Generator")

    # Define available arguments
    parser.add_argument(
        "--image",
        type=str,
        required=True,
        help="Path or URL to the image to caption"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="Controls creativity (lower = deterministic, higher = creative)"
    )
    parser.add_argument(
        "--top_k",
        type=int,
        default=50,
        help="Limit next-word choices to top K most likely options"
    )
    parser.add_argument(
        "--top_p",
        type=float,
        default=0.9,
        help="Nucleus sampling: keep top tokens covering P probability mass"
    )
    parser.add_argument(
        "--max_new_tokens",
        type=int,
        default=50,
        help="Maximum number of tokens to generate for the caption"
    )

    # Parse arguments from the command line
    args = parser.parse_args()

    # 2️⃣ Generate the caption
    print("\n🔍 Generating caption...\n")
    caption = generate_caption(
        image_input=args.image,
        temperature=args.temperature,
        top_k=args.top_k,
        top_p=args.top_p,
        max_new_tokens=args.max_new_tokens
    )

    # 3️⃣ Print the result
    print("🖼️  Image:", args.image)
    print(f"💬  Caption: {caption}\n")

if __name__ == "__main__":
    main()
