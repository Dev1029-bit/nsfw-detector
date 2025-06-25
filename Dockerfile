# Use Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install required system packages including git
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    libgl1-mesa-glx \
 && rm -rf /var/lib/apt/lists/* \
 && pip install --upgrade pip \
 && pip install --retries 10 --timeout 60 --no-cache-dir -r requirements.txt


# Copy the rest of the application
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run the API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
