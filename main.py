from fastapi import FastAPI, Body, Depends, HTTPException, status
import shutil
from hmac import compare_digest
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
import subprocess
from git import Repo
from pathlib import Path
import os
import composer
from contextlib import asynccontextmanager

description = """
This Application handles container & instance creation for the CTF Citadel Platform
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    DOCKERHUB_USERNAME = os.getenv("DOCKERHUB_USERNAME")
    DOCKERHUB_TOKEN = os.getenv("DOCKERHUB_TOKEN")

    # login to dockerhub
    subprocess.run(["docker", "login", "-u", DOCKERHUB_USERNAME, "-p", DOCKERHUB_TOKEN])

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
    version="0.0.6",
    description=description
)

def auth(
    token: HTTPAuthorizationCredentials = Depends(HTTPBearer(scheme_name="PSK")),
) -> bool:
    BEARER = token.credentials
    PSK = os.getenv("PSK") or ""
    if compare_digest(BEARER, PSK):
        return True
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.get("/", tags=["misc"])
async def root():
    return {"message": "Hello Hacker, Welcome to the CTF Citadel Infra Controller! Wrong place to be if you're looking for flags though. Good luck!"}

@app.post("/challenge", tags=['challenges'], dependencies=[Depends(auth)])
async def spawn_challenge(
    challenge: str = Body(..., embed=True),
    environment_variables: Optional[str] = Body(..., embed=False)
):
    """
    This function can be used to spawn new containers according to a specified compose file
    """
    return await composer.spawn_challenge(challenge, environment_variables)

@app.delete("/container", tags=['containers'], dependencies=[Depends(auth)])
async def delete_container(container_id: str):
    """
    This endpoint deletes a specified container/stack.
    """
    completed_process = subprocess.run(["docker", "stack", "rm", container_id], capture_output=True)
    code = completed_process.returncode
    return {"message": f"Deleted container {container_id} (Exit Code: {code})"}

@app.get("/challenges", tags=['challenges'], dependencies=[Depends(auth)])
async def challenge_list():
    """
    This endpoint returns a list of all challenges
    """
    challenges = []
    # add all challenges from challenges/ to the list
    for challenge in os.listdir('challenges/'):
        challenges.append(challenge)
    return challenges
