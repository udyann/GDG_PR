import streamlit as st
import requests
import os

st.sidebar.header("Text to Image")
prompt = st.text_input("Enter a prompt for the image:")

if st.button("generate image"):
    with st.spinner(text="generating image..."):
        url = "http://" + str(os.getenv("FASTAPI_HOST", "127.0.0.1")) + ":"+ str(os.getenv("FASTAPI_PORT", 8000)) + "/text-to-image"
        response = requests.post(url=url, json={"prompt":prompt})
        if response.status_code == 200:
            # Load image from the response
            st.image(response.content, caption=f"Generated Image for: {prompt}", use_container_width=True)
        else:
            st.error("Failed to generate image!")