# CTF Citadale Infra Controller

# Starting local instance
```
pip install -r requirements.txt (maybe in an env)
uvicorn main:app --host 0.0.0.0
```

basically good to go.

# Setup Docker Swarm

Initialize Cluster:
```bash
docker swarm init --advertise-addr <MANAGER-IP>
```
This will return somethin like:
```bash
docker swarm init --advertise-addr 192.168.99.100
Swarm initialized: current node (dxn1zf6l61qsb1josjja83ngz) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \
    192.168.99.100:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```
As the output suggests, you need to run the `docker swarm join --token <TOKEN>` command on each node.


As by: https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/

# Setup Traefik in newly created Swarm
```bash
docker network create --driver=overlay traefik-public
```
```bash
export NODE_ID=$(docker info -f '{{.Swarm.NodeID}}')
```
```bash
docker node update --label-add traefik-public.traefik-public-certificates=true $NODE_ID
```
```bash
export EMAIL=admin@tophack.at
export DOMAIN=traefik.cluster.tophack.at
export USERNAME=admin
export PASSWORD=changethis
export HASHED_PASSWORD=$(openssl passwd -apr1 $PASSWORD)
export CF_API_EMAIL=email_of_your_cf_account
export CF_API_KEY=cloudflare_api_key
```

```bash
docker stack deploy -c traefik-v3.yml traefik
```
Deploy the freshly configured Traefik to the cluster.

As by: https://dockerswarm.rocks/traefik/