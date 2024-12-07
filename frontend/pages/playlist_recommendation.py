import streamlit as st
import requests
import os

st.sidebar.header("Travel Playlist Recommendation")

imageURL = st.text_input("Please provide an URL of image you are traveling.")

if st.button("label"):
    url = "http://" + str(os.getenv("FASTAPI_HOST", "127.0.0.1")) + ":"+ str(os.getenv("FASTAPI_PORT", 8000)) + "/image-to-text"

    res = requests.post(url=str(url), json= {"url": imageURL})
    st.subheader(f"{res.text}")