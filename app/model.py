from nsfw_detector import predict
from app.utils import load_config

config = load_config()
MODEL_PATH = config["model_path"]
NSFW_THRESHOLD = config["nsfw_threshold"]
FLAG_MIN, FLAG_MAX = config.get("intermediate_flag_range", [0.2, 0.4])

model = predict.load_model(MODEL_PATH)

CATEGORIES = ["drawings", "hentai", "neutral", "porn", "sexy"]

def classify_image(image_array) -> dict:
    predictions = model.predict(image_array)[0]
    scores = dict(zip(CATEGORIES, predictions))
    nsfw_score = scores["porn"] + scores["sexy"] + scores["hentai"]

    if nsfw_score >= NSFW_THRESHOLD:
        status = "blocked"
        label = "nsfw"
    elif FLAG_MIN <= nsfw_score < NSFW_THRESHOLD:
        status = "flagged"
        label = "nsfw"
    else:
        status = "approved"
        label = "safe"

    return {
        "label": label,
        "status": status,
        "nsfw_score": round(float(nsfw_score), 4),
        "scores": {k: round(float(v), 4) for k, v in scores.items()}
    }