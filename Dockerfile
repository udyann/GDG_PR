FROM python:3.12-slim

RUN apt-get update && apt-get install -y libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/ .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# RUN python -c "from transformers import CLIPProcessor, CLIPModel; CLIPModel.from_pretrained('openai/clip-vit-base-patch16'); CLIPProcessor.from_pretrained('openai/clip-vit-base-patch16')"

# COPY app/ .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]