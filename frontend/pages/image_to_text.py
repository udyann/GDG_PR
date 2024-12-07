import streamlit as st
import requests
import os

st.sidebar.header("Image to Text")

imageURL = st.text_input("Please provide an image URL.")
input_labels = st.text_input("Please provide possible labels. Default: cat, dog, car, airplane")
labels = input_labels.split(",")

if st.button("label"):
    url = "http://" + str(os.getenv("FASTAPI_HOST", "127.0.0.1")) + ":"+ str(os.getenv("FASTAPI_PORT", 8000)) + "/image-to-text"
    if labels[0] != '':
        res = requests.post(url=str(url), json= {"url": imageURL, "labels": labels})
    else:
        res = requests.post(url=str(url), json= {"url": imageURL, "labels": ["cat", "dog", "car", "airplane"]})

    st.subheader(f"{res.text}")