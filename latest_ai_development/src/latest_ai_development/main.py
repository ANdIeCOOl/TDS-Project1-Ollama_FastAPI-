#!/usr/bin/env python
import sys
import warnings
import asyncio
import logging

from datetime import datetime

from latest_ai_development.crew import LatestAiDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import uvicorn
import openai
import logging

# FastAPI app definition
app = FastAPI()

# Define a Pydantic model for the task input
class TaskRequest(BaseModel):
    task: str

# Route to check server health
@app.get("/")
async def index():
    return {"message": "Hello, the FastAPI server is running!"}

@app.post("/run")
async def run_task(task: str):
    logging.info(f"Running task: {str}")
    try:
        # Run the crew kickoff asynchronously
        asyncio.create_task(run_crew(task))
        return {"message": f"Executing task: {task}"}
    except Exception as e:
        return {"error": str(e)}

async def run_crew(task: str):
    """
    This will run the crew in a separate thread to avoid blocking FastAPI.
    """
    logging.info(f"Starting crew task: {task}")
    try:
        # Pass the task input to the crew kickoff
        inputs = {'topic': task}
        LatestAiDevelopment().crew().kickoff(inputs=inputs)
    except Exception as e:
        logging.error(f"Error during crew kickoff: {str(e)}")

# Endpoint to read a file
@app.get("/read")
async def read_file(path: str):
    try:
        with open(path, 'r') as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        logging.error(f"Error reading file {path}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error reading file: {str(e)}")


# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     logging.info("Starting FastAPI server...")
#     uvicorn.run(app, host="0.0.0.0", port=8000)
#     inputs = {
#         'topic': 'Why is the sky blue?'
#     }
    
#     try:
#         LatestAiDevelopment().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")

def run():
    """
    Run the FastAPI server and crew tasks concurrently.
    """
    logging.info("Starting FastAPI server...")
    
    # Start the FastAPI server
    asyncio.run(uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info"))

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        LatestAiDevelopment().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LatestAiDevelopment().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        LatestAiDevelopment().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
