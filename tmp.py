import docker

docker_client = docker.from_env()
container = docker_client.containers.list(filters={"name": "27995ea4-92fa-424e-96c1-9220de96824d"})
print(container)
print(docker_client.containers.get(container[0].id).status)