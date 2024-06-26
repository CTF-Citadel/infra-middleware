# CTF-Citadel Infra Controller

# Starting local instance

Just run

```bash
pip install -r requirements.txt # python -m venv env && source env/bin/activate
uvicorn main:app --host 0.0.0.0
```

basically good to go.

# Setup Docker Swarm production environment

This setup requires a Linux machine with Docker installed.

## Initialize Cluster:

```bash
docker swarm init --advertise-addr <MANAGER-IP>
```

This will return something like:

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

## Setup Traefik in newly created Swarm

```bash
docker network create --driver=overlay --subnet=10.1.0.0/16 traefik-public
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
export CONTROLLER_DOMAIN=cluster.tophack.at
export USERNAME=admin
export PASSWORD=changethis
export HASHED_PASSWORD=$(openssl passwd -apr1 $PASSWORD)
export CF_API_EMAIL=email_of_your_cf_account
export CF_API_KEY=cloudflare_api_key
export GITHUB_USERNAME=CTF-Citadel
export GITHUB_TOKEN=super_secret_token
export DOCKERHUB_USERNAME=ctf-citadel
export DOCKERHUB_TOKEN=super_secret_token
export PSK=Trombone-Droop9-Falsify-Superbowl-Overload
```

```bash
docker login -u $GITHUB_USERNAME -p $GITHUB_TOKEN ghcr.io
```

Login to ghcr.io for the controller image

```bash
docker stack deploy -c tophack-stack.yml tophack-stack
```

This deploys Traefik and the infra-middleware controller to the Swarm cluster with your environment variables

As per: https://dockerswarm.rocks/traefik/
