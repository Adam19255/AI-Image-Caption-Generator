from fastapi import APIRouter, UploadFile, File, Query
from PIL import Image
from io import BytesIO
from captioner.inference import generate_caption

router = APIRouter(prefix="/caption", tags=["Caption"])

@router.post("/")
async def caption_image(
    file: UploadFile = File(...),
    temperature: float = Query(1.0, ge=0.1, le=2.0, description="Creativity level")
):
    """
    Generate a caption from an uploaded image with adjustable creativity.
    """
    try:
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert("RGB")

        caption = generate_caption(
            image_input=image,
            temperature=temperature
        )

        return {"caption": caption, "temperature": temperature}
    except Exception as e:
        return {"error": str(e)}
