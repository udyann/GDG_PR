import streamlit as st
import requests
import os

st.sidebar.header("Travel Playlist Recommendation")

imageURL = st.text_input("Please provide an URL of image you are traveling.")
genre = st.text_input("Optional) Any preferred genre?")
travelLabels = ["nature", "city", "summer", "winter", "bright", "dark", "classic", "modern"]

if st.button("label"):
    url = "http://" + str(os.getenv("FASTAPI_HOST", "127.0.0.1")) + ":"+ str(os.getenv("FASTAPI_PORT", 8000)) + "/playlist-recommendation"
    if not genre:
        genre = ""
    res = requests.post(url=str(url), json= {"url": imageURL, "labels": travelLabels, "genre": genre}).json()
    
    videos = []
    for each in res['items']:
        print(each)
        snippet = each['snippet']
        if 'videoId' in each['id']:
            videos.append([each['id']['videoId'], snippet['title'], snippet['thumbnails']['medium']['url']])
        else:
            continue
    
    row1 = st.columns(len(videos)//2)
    row2 = st.columns(len(videos)-len(videos)//2)
    grid = [col.container(height=400) for col in row1+row2]
    for i in range(len(videos)):
        with grid[i]:
            st.title(videos[i][1])
            st.image(videos[i][2])
            video_url = "https://youtube.com/watch?v="+videos[i][0]
            st.markdown(f"[click to play]{video_url}")
    st.subheader("Enjoy!")