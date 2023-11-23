from fastapi import FastAPI
import composer
import docker
import json
import aiohttp
import asyncio
import os
import zipfile
from contextlib import asynccontextmanager
import config

description = """
This Application handles container & instance creation for the CTF Citadel Platform
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    #downlaod tarball
    yield
    async with aiohttp.ClientSession() as session:
        async with session.get(config.challenge_repo_tarball) as response:
            if response.status == 200:
                with open('challenges/challenges.zip',mode='wb') as file:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        file.write(chunk)
    #unzip downloaded challenges
    with zipfile.ZipFile('challenges/challenges.zip','r') as zip_ref:
        print("grr")
        zip_ref.extractall('challenges/')

    yield


app = FastAPI(lifespan=lifespan,
    title="CTF Citadel Infra Controller",
    version="0.0.3",
    description=description
              )


@app.get("/",tags=["misc"])
async def root():
    return {"message": "Hello Hacker"}

@app.post("/challenge",tags=['challenges'])
async def spawn_challenge(compose_file: str, environment_variables: str | None = None):
    """
        This function can be used to spawn new containers according to a specified compose file
    """
    return composer.spawn_challenge(compose_file, environment_variables)

@app.get("/container",tags=['containers'])
async def container_details(container_id: str):
    """
        This endpoint returns infos about a specified container. Such as environment variables
        WIP: Currently just returning the name
    """
    docker_client = docker.from_env()
    container = docker_client.containers.get(container_id)
    return container.name

@app.get("/containers",tags=['containers'])
async def container_details():
    """
        This endpoint returns a list of all containers
    """
    docker_client = docker.from_env()
    list_of_containers = []
    for container in docker_client.containers.list():
        list_of_containers.append(container.id)
    return list_of_containers


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