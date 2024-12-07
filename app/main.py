from fastapi import FastAPI, Response, File, UploadFile
#from fastapi.responses import StreamingResponse
import uvicorn
from models import ImageToTextModel
import urllib.parse
import requests
from pydantic import BaseModel
import os

app = FastAPI()

class URLRequest(BaseModel):
    url: str

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
    prediction = model.predict(imageURL=url)
    return f"it looks like {prediction}"


#local test
if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("FASTAPI_PORT", "127.0.0.1"), port=int(os.getenv("FASTAPI_PORT", 8000)))