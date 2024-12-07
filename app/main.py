from fastapi import FastAPI, Response
from dotenv import load_dotenv
import uvicorn
from models import ImageToTextModel
import urllib.parse
import requests
from pydantic import BaseModel
import os

app = FastAPI()
load_dotenv()

class URLRequest(BaseModel):
    url: str
    labels: list

class PLRequest(BaseModel):
    url: str
    genre: str
    labels: list

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    return {"status": "Healthy ^-^"}

@app.post("/text-to-image")
def text_to_image(request: PromptRequest):
    prompt = request.prompt
    encoded_prompt = urllib.parse.quote_plus(prompt, safe="")
    url = "https://image.pollinations.ai/prompt/" + encoded_prompt
    response = requests.get(url)
    if response.status_code == 200:
        return Response(content=response.content, media_type="image/jpeg")
    else:
        return {"error": "failed to generate image T^T"}


@app.post("/image-to-text")
async def image_to_text(request: URLRequest):
    model = ImageToTextModel()

    url = request.url
    if request.labels:
        labels = request.labels
        prediction = model.predict(imageURL=url, labels=labels)
    else:
        prediction = model.predict(imageURL=url)
    return f"it looks like {prediction}"

@app.post("/playlist-recommendation")
async def playlist_recommendation(request: PLRequest):
    model = ImageToTextModel()

    url = request.url
    labels = request.labels
    if len(request.genre) >= 2:
        genre = request.genre
    else:
        genre = ""

    moodPrediction = model.predict(imageURL=url, labels=labels)
    PLQuery = moodPrediction + " " + genre + " playlist"
    PLParams = {
        "key": os.getenv("GOOGLE_API_KEY"),
        "q": PLQuery,
        "part": "snippet",
        "maxResults": 4
    }
    PLParams = PLParams
    response = requests.get("https://www.googleapis.com/youtube/v3/search", params=PLParams)
    response_json = response.json()
    return response_json

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("FASTAPI_PORT", "127.0.0.1"), port=int(os.getenv("FASTAPI_PORT", 8000)))