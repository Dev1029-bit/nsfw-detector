# 🔞 NSFW Image Detection Microservice (Offline + Ethical)

A clean, lightweight NSFW image classification microservice built with **FastAPI** and a **pre-trained MobileNet v2 model** (Gantman). This project is designed for **offline usage**, **ethical testing**, and **academic demonstration** only — no real NSFW imagery is used or supported.

---

## 📌 Project Purpose

This microservice is built for:

* ✅ Ethical moderation testing
* ✅ Base64 image classification (safe or NSFW)
* ✅ Local-only execution (no cloud hosting)
* ✅ Academic or showcase purposes
* ❌ No real NSFW or explicit content

---

## 🧠 Model & Categories

The model classifies images into 5 categories:

* `drawings`
* `hentai`
* `neutral`
* `porn`
* `sexy`

Your **`nsfw_score`** is calculated as:

```python
nsfw_score = porn + sexy + hentai
```

Then classified using threshold logic from `config.json`.

---

## 🗂️ Project Structure

```
nsfw_detector_core/
│
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── model.py          # Model prediction and scoring logic
│   ├── utils.py          # Base64 decoding, preprocessing, config loader
│   └── schemas.py        # Pydantic models for request and response
│
├── config.json           # Configuration for model thresholds and path
├── Dockerfile            # Docker image definition
├── requirements.txt      # Python dependencies list
├── README.md             # Project documentation
│
├── model/
│   └── saved_model.h5    # Pre-trained MobileNetV2 NSFW classifier
│
├── datasets/             # Local image datasets (used for evaluation)
│   └── safe/             # Manually curated safe images (e.g., from Unsplash)
│       ├── safe_1.jpg
│       ├── safe_2.jpg
│       └── ...
```

---

## ⚙️ Configuration: `config.json`

```json
{
  "model_path": "model/saved_model.h5",
  "nsfw_threshold": 0.4,
  "intermediate_flag_range": [0.2, 0.4]
}
```

---

## 🚀 Local Setup

### ✅ Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Then visit:

```
http://localhost:8000/docs
```

---

## 🐳 Docker Setup (Simple Dockerfile-Only)

> Only for **local demo purposes** — no cloud hosting required

### 1️⃣ Build the image

```
docker build -t nsfw-detector-app .
```

### 2️⃣ Run the container

```
docker run -p 8000:8000 nsfw-detector-app
```

### 3️⃣ Access the Swagger UI

```
http://localhost:8000/docs
```

---

✅ How to Use POST /check-image

Input Format: Send a valid image (e.g., .jpg, .png) as a Base64-encoded string in a JSON payload:

{
  "user_id": "stu_3092",
  "image_base64": "<your_base64_string_here>"
}

user_id: any unique string identifying the user

image_base64: must be the raw base64 string only (exclude data:image/...;base64, prefix)

How to Convert Your Image to Base64:

Visit https://www.base64-image.de/

Upload your image file

Copy only the Base64 content (ignore the data:image/... part)

Paste the string in the image_base64 field in Swagger UI

How to Test via Swagger UI:

Go to http://localhost:8000/docs

Expand POST /check-image

Click Try it out

Fill in the JSON body with user_id and valid image_base64

Click Execute to receive classification

Expected Output:**

{
  "user_id": "stu_3092",
  "nsfw_score": 0.88,
  "label": "nsfw",
  "threshold": 0.55,
  "status": "blocked"
}

label: safe / nsfw

status: approved / flagged / blocked based on score range

threshold: fetched from config.json

---

### Example Output

```json
{
  "user_id": "stu_3092",
  "nsfw_score": 0.88,
  "label": "nsfw",
  "threshold": 0.4,
  "status": "blocked"
}
```

---

## 🔐 Ethical Considerations

> This project does **not** involve real explicit images.

* ✅ NSFW images used are **synthetic, blurred, or anime-style**
* ❌ No real pornographic content allowed
* ✅ Safe categories include **drawings** and **neutral**
* ✅ Complies with offline moderation research policies

---

## 🎓 Ideal For

* Student & academic demos
* Responsible AI demonstrations
* Local moderation tools
* FastAPI + ML portfolio projects

---

## 🧪 Testing Tips

* Use Swagger UI or Postman
* Supply `base64` images under 512KB
* Test `nsfw`, `flagged`, and `safe` examples


---

## 📄 License

MIT License – For academic, ethical, and personal use.

---

## 🙏 Credits

* [Gantman NSFW Model](https://github.com/GantMan/nsfw_model)
* [FastAPI Framework](https://fastapi.tiangolo.com/)
* TensorFlow, NumPy, Pillow

---

> 🔒 Built for responsible use only. No explicit content is included, supported, or allowed.
