from fastapi import FastAPI,Response
import requests

app = FastAPI()
ollama_model = "deepseek-r1:1.5b"
ollama

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/ask")
def ask(prompt: str):
    response = requests.post("http://localhost:11434/api/generate",  #ollama runs on this port 
        json={ "prompt": prompt,
                "stream": False,
                "model" : "deepseek-r1:1.5b"

            } )

    return Response(content=response.text, media_type="application/json")

    