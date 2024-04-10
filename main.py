from fastapi import FastAPI, Body, Depends, HTTPException, status
from pydantic import BaseModel
from hmac import compare_digest
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
import subprocess
from git import Repo
from pathlib import Path
import os

description = """
This Application handles container & instance creation for the CTF Citadel Platform
"""

app = FastAPI(
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
    return {"message": "Spawn challenge"}

@app.delete("/container", tags=['containers'], dependencies=[Depends(auth)])
async def delete_container(container_id: str):
    """
    This endpoint deletes a specified container/stack.
    """
    return {"message": f"Deleted container {container_id}"}

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
