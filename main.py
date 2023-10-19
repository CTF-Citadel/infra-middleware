from fastapi import FastAPI
import composer
import aiohttp
import asyncio
import zipfile
from contextlib import asynccontextmanager
import config

@asynccontextmanager
async def lifespan(app: FastAPI):
    #downlaod tarball
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


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello Hacker"}

@app.post("/container")
async def spawn_challenge(compose_file: str, environment_variables: dict):
    """
        This function can be used to spawn new containers according to a specified compose file
    """
    return composer.spawn_challenge(compose_file, environment_variables)

@app.get("/container")
async def container_details(container_id: str):
    """
        This endpoint returns infos about a specified container. Such as environment variables
    """