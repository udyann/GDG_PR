from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
from io import BytesIO

import requests # added for localTest



class ImageToTextModel():
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")
        self.labels = ["cat", "dog", "car", "airplane"]
    
    def predict(self, imageURL):
        image = Image.open(requests.get(imageURL, stream=True).raw)
        inputs = self.processor(text=self.labels, images=image, return_tensors="pt", padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits_per_image = outputs.logits_per_image
            probs = logits_per_image.softmax(dim=1)
        
        #return most relevant label
        maxLabel = self.labels[0]
        maxProb = probs[0][0].item()
        for label, prob in zip(self.labels, probs[0]):
            if prob > maxProb:
                maxProb = prob
                maxLabel = label
            print(f"{label}: {prob.item() * 100:.2f}%")
        return maxLabel
        

class TextToImageModel():
    def __init__(self):
        self.pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
        self.pipe = self.pipe.to("cuda")
    
    def generateImage(self, prompt):
        p = prompt
        image = self.pipe(p).images[0]
        try:
            image = self.pipe(p).images[0]
            
            # Convert the image to BytesIO format
            img_byte_arr = BytesIO()
            image.save(img_byte_arr, format="PNG")
            img_byte_arr.seek(0)  # Reset stream position for reading
            
            return img_byte_arr
        except Exception as e:
            # Log or handle errors gracefully
            print(f"Error generating image: {e}")
            raise RuntimeError("Image generation failed.") from e
