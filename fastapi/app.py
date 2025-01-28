from fastapi import FastAPI,Response
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/ask")
def ask(prompt: str):
    response = requests.post("http://localhost:11434/api/generate", 
        json={ "prompt": prompt,
                "stream": False,
                "model" : "deepseek-r1:1.5b"

            } )

    return Response(content=response.text, media_type="application/json")

    