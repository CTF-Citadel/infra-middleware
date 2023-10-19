from fastapi import FastAPI
import composer

app = FastAPI()


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