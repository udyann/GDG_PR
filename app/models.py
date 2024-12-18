from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import os
import requests

default_labels = ["cat", "dog", "car", "airplane"]

class ImageToTextModel():
    def __init__(self):
        clip_model = os.getenv("CLIP_MODEL_NAME", default="openai/clip-vit-base-patch16")
        self.model = CLIPModel.from_pretrained(clip_model)
        self.processor = CLIPProcessor.from_pretrained(clip_model)
    
    def predict(self, imageURL, labels = default_labels):
        image = Image.open(requests.get(imageURL, stream=True).raw)
        inputs = self.processor(text=labels, images=image, return_tensors="pt", padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits_per_image = outputs.logits_per_image
            probs = logits_per_image.softmax(dim=1)
        
        #return most relevant label
        maxLabel = labels[0]
        maxProb = probs[0][0].item()
        for label, prob in zip(labels, probs[0]):
            if prob > maxProb:
                maxProb = prob
                maxLabel = label
            print(f"{label}: {prob.item() * 100:.2f}%")
        return maxLabel
        
#not used anymore
'''
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
'''