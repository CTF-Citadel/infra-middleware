import subprocess
import uuid
import os
import shutil
import json
import helper
import socket
def spawn_challenge(challenge, environment_variables=None):
    """
    Spawn a new instance of a challenge.
    :param challenge: provide the name of the docker-compose file for the challenge"
    :param environment_variables: provide the environment variables for the docker-compose file as dictionary.
    :return: output of detached compose command
    """
    try:
        response = {"message": "error"}
        instance_id = str(uuid.uuid4())
        path_to_compose_file = "challenges/" + challenge
        #copy compose file to instance folder
        shutil.copytree(path_to_compose_file, "instances/" + instance_id)

        #create instance network
        #subprocess.run(["docker", "network", "create", instance_id])
        #generate a random unique network port for the web app
        environment_variables = json.loads(environment_variables)
        port = helper.get_port()
        environment_variables["PORT"] = str(port)
        #build a response that returns instance id, challenge and all env vars
        subprocess.run(["docker-compose", "-f", "instances/" + instance_id + "/docker-compose.yml", "up","-d"], env=environment_variables)
        environment_variables["IP"] = str(socket.gethostbyname(socket.gethostname()))
        response = {
            "instance_id": instance_id,
            "challenge": challenge,
            "details": environment_variables
        }
        return response
    except Exception as e:
        return {"error": str(e)}