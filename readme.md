# GenAI360 Azure향 개발지원 위한 FastAPI
## FastAPI Project 구성 과정
1. fastAPI 설치
```shell
pip install fastapi
```
2. Svelte 설치하기
```shell
# 설치 명령어
npm create vite@latest frontend -- --template svelte

# frontend디렉토리 이동 후 Svelte 서버 실행
npm run dev
```

3. uvicorn 설치하기
```shell
# 설치 명령어
pip install "uvicorn[standard]"

# App디렉토리 이동 후 FastAPi 서버 실행
uvicorn main:app --reload
```

4. 화면구동을 위한 Jinja템플릿엔진 설치
```shell
pip install jinja2
```

5. LLM 실습을 위한 라이브러리 설치
```shell
pip install langchain
pip install openai
```

## FastAPI 실행
```shell
# Dev
uvicorn main:app --reload
# Web Publishing
uvicorn theme:app --reload
```

* 추가사항(Azure OpenAI)
기능개발 후 버튼을 통해 선택할 수 있도록
GPT4o       : 높은 지능이 필요한 경우 선택
GPT4oMini   : 개발진행



- Embedding model
    - small
    - large