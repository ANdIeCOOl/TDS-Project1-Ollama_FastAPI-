from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

    @app.get("/")
    async def index():
        return {"message": "Hello"}


@app.post("/run")
@app.post("/run")
async def run_task(task: str):
    print(task)
    print("0-0-0"*100)
    return {"message": f"Executing task: {task}"}
    
    
    return {"result": result}

@app.get("/read")
async def read_file(path: str):
    try:
        with open(path, 'r') as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        return {"error": str(e)}