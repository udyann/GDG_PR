from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

import requests # added for localTest

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

class TextToImageModel():
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")



class ImageToTextModel():
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")
        self.labels = ["cat", "dog", "car", "airplane"]
    
    def predict(self, imageURL):
        image = Image.open(requests.get(imageURL, stream=True).raw)
        inputs = self.processor(text=self.labels, images=image, return_tensors="pt", padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
            logits_per_image = outputs.logits_per_image
            probs = logits_per_image.softmax(dim=1)
        for label, prob in zip(self.labels, probs[0]):
            print(f"{label}: {prob.item() * 100:.2f}%")
        