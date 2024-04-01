from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
import composer
import docker
import json
import aiohttp
import asyncio
import os
import zipfile
from contextlib import asynccontextmanager
import config
from typing import Optional
import subprocess
from git import Repo
from pathlib import Path
import shutil

description = """
This Application handles container & instance creation for the CTF Citadel Platform
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    shutil.rmtree('challenges/', ignore_errors=True)
    Repo.clone_from(f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/CTF-Citadel/challenges.git", 'challenges/')
    def remove_non_directories(directory_path):
        """
        Removes all non-directory files from the specified directory.
        """
        directory = Path(directory_path)
        for item in directory.iterdir():
            if item.is_file():
                item.unlink()

    # Remove all non-directory files from the challenges directory. (e.g. examples, README.md, etc.)
    remove_non_directories('challenges/')

    yield


app = FastAPI(lifespan=lifespan,
    title="CTF Citadel Infra Controller",
    version="0.0.5",
    description=description
              )


@app.get("/",tags=["misc"])
async def root():
    return {"message": "Hello Hacker, Welcome to the CTF Citadel Infra Controller! Wrong place to be if you're looking for flags though. Good luck!"}

@app.post("/challenge", tags=['challenges'])
async def spawn_challenge(
    challenge: str = Body(..., embed=True),
    environment_variables: Optional[str] = Body(..., embed=False)
):
    """
    This function can be used to spawn new containers according to a specified compose file
    """
    return composer.spawn_challenge(challenge, environment_variables)

@app.get("/container",tags=['containers'])
async def container_details(container_id: str):
    """
        This endpoint returns infos about a specified container. Such as environment variables
        WIP: Currently just returning the name
    """
    completed_process = subprocess.run(["docker", "stack", "ps", container_id], capture_output=True)
    output = completed_process.stdout.decode('utf-8')

    return {"output": output}

@app.delete("/container",tags=['containers'])
async def container_details(container_id: str):
    """
        This endpoint returns infos about a specified container. Such as environment variables
        WIP: Currently just returning the name
    """
    completed_process = subprocess.run(["docker", "stack", "rm", container_id], capture_output=True)
    output = completed_process.stdout.decode('utf-8')

    return {"output": output}



@app.get("/challenges",tags=['challenges'])
async def challenge_list():
    """
        This endpoint returns a list of all challenges
    """
    challenges = []
    #add all challenges from challenges/ to the list
    for challenge in os.listdir('challenges/'):
        challenges.append(challenge)
    return challenges