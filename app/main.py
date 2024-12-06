from fastapi import FastAPI
import uvicorn
from models import TextToImageModel, ImageToTextModel

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

@app.get("/image-to-text")
async def image_to_text():
    model = ImageToTextModel()
    prediction = model.predict("https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/272px-Cat_August_2010-4.jpg")
    return {"message": f"it looks like {prediction}"}


#local test
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)