import numpy as np
from PIL import Image, ImageOps
from core.constants import IMAGE_SIZE


def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Resize, normalize and prepare image for model input.
    - Resize to 224x224
    - Convert to RGB
    - Normalize to [-1, 1]
    - Add batch dimension
    """
    image = ImageOps.fit(image, IMAGE_SIZE, Image.Resampling.LANCZOS)
    image = image.convert("RGB")
    img_array = np.asarray(image, dtype=np.float32)
    img_array = (img_array / 127.5) - 1
    return np.expand_dims(img_array, axis=0)
