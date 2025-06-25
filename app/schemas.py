# app/schemas.py
from pydantic import BaseModel

class ImageBase64Request(BaseModel):
    user_id: str
    image_base64: str

class PredictionResponse(BaseModel):
    user_id: str
    nsfw_score: float
    label: str
    threshold: float
    status: str
