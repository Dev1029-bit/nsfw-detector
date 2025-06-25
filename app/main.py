# app/main.py
from fastapi import FastAPI
from app.schemas import ImageBase64Request, PredictionResponse
from app.utils import preprocess_base64_image, load_config
from app.model import classify_image

app = FastAPI(title="NSFW Detection API")

config = load_config()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"model_path": config["model_path"], "threshold": config["nsfw_threshold"]}

@app.post("/check-image", response_model=PredictionResponse)
def check_image(payload: ImageBase64Request):
    image_array = preprocess_base64_image(payload.image_base64)
    prediction = classify_image(image_array)

    return PredictionResponse(
        user_id=payload.user_id,
        nsfw_score=prediction["nsfw_score"],
        label=prediction["label"],
        threshold=config["nsfw_threshold"],
        status=prediction["status"]
    )
