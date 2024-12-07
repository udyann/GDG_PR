from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
from models import TextToImageModel, ImageToTextModel
from pydantic import BaseModel # hmmm..... delete????

app = FastAPI()

class PromptRequest(BaseModel): ### hmmm... delete????
    prompt: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    return {"status": "Healthy ^-^"}

@app.post("/text-to-image")
#def text_to_image(prompt: str): #original
def text_to_image(request:PromptRequest): ## hmmmmmmmmmmmmmmm......
    print("wtf")
    model = TextToImageModel()
    prompt = request.prompt ## hmmmmmmmmmmm.........
    image_stream = model.generateImage(prompt= prompt)
    return StreamingResponse(image_stream, media_type="image/png")

@app.post("/image-to-text")
async def image_to_text(url: str):
    model = ImageToTextModel()
    prediction = model.predict(imageURL=url)
    return {"message": f"it looks like {prediction}"}


#local test
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)