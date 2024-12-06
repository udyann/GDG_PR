from fastapi import FastAPI
from models import TextToImageModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    return {"status": "Healthy ^-^"}

@app.post("/text-to-image")
def text_to_image(text: str):
    return {"message": f"requested image for {text}"}