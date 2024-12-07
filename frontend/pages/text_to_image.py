import streamlit as st
from PIL import Image
from io import BytesIO
import requests

st.sidebar.header("Text to Image")
prompt = st.text_input("Enter a prompt for the image:")

if st.button("generate image"):

    response = requests.post("http://127.0.0.1:8000/text-to-image", json={"prompt": prompt})
    if response.status_code == 200:
        # Load image from the response
        img = Image.open(BytesIO(response.content))
        st.image(img, caption=f"Generated Image for: {prompt}")
    else:
        st.error("Failed to generate image!")