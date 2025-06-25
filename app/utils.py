import base64
import numpy as np
import json
from io import BytesIO
from PIL import Image

def load_config(path="config.json"):
    with open(path, "r") as f:
        return json.load(f)

def preprocess_base64_image(base64_str: str, target_size=(224, 224)) -> np.ndarray:
    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data)).convert("RGB")
    image = image.resize(target_size)
    image_array = np.asarray(image).astype("float32") / 255.0
    return np.expand_dims(image_array, axis=0)