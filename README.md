# GDG_PR

## 주요 기능
1. 외부 API (pollinations.ai)를 활용한 기초적인 Text To Image
2. CLIP을 활용하여 이미지 url과 가능한 label들을 넘기면 분류해주는 기초적인 Image To Text
3. Image To Text를 활용하여 여행지의 사진을 올리면 어울리는 플레이리스트를 찾아주는 Playlist Recommendation

## How To Run

### 1. Locally
1. 해당 디렉토리 clone
2. 터미널에 pip install -r ./app/requirements.txt
3. https://console.cloud.google.com/apis/library/youtube.googleapis.com 접속하여 API 키 생성 (무료)
4. app 디렉토리 안에  .env 파일 생성 후    
CLIP_MODEL_NAME=openai/clip-vit-base-patch16   
FASTAPI_HOST=0.0.0.0   
FASTAPI_PORT=8000   
STREAMLIT_HOST=localhost   
STREAMLIT_PORT=8501   
GOOGLE_API_KEY={3번에서 생성한 api key}   
(default setting입니다.)   
6. 터미널에 uvicorn main:app --host=0.0.0.0 --port=8000
7. 새로운 터미널 열어서, streamlit run ./frontend/app.py

### 2. Docker
1. Docker Image: https://hub.docker.com/r/udyann/gdg-pr/tags pull
2. 컨테이너 실행    
$ docker run -p 8000:8000 --env-file ./app/.env {image id}
3. 새로운 터미널 열어서,    
streamlit run ./frontend/app.py

### .env 파일을 image에 구워버려서... 후딱 수정을 해야 합니다.
