import streamlit as st
import requests

st.sidebar.header("Image to Text")

imageURL = st.text_input("Please provide an image URL.")

if st.button("label"):
    param = {'url': imageURL}
    res = requests.post(url = "http://127.0.0.1:8000/image-to-text", params= param)
    st.subheader(f"{res.text}")