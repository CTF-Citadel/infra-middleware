from fastapi import FastAPI
import composer

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Hacker"}

@app.post("/container")
async def spawn_container(compose_file: str):
    """
        This function can be used to spawn new containers according to a specified compose file
    """
    return composer.spawn_container(compose_file)

