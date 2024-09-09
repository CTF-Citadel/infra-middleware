import subprocess
import uuid
import shutil
import json
import socket

async def spawn_challenge(challenge, environment_variables=None):
    """
    Spawn a new instance of a challenge.

    :param challenge: provide the name of the docker-compose file for the challenge
    :param environment_variables: provide the environment variables for the docker-compose file as a dictionary
    :return: output of detached compose command
    """
    try:
        instance_id = str(uuid.uuid4())
        print(f"{instance_id} - {challenge} - {environment_variables} - started")
        path_to_compose_file = "challenges/" + challenge
        # copy compose file to instance folder
        shutil.copytree(path_to_compose_file, "instances/" + instance_id)
        
        if environment_variables is None:
            environment_variables = {}
        environment_variables = json.loads(environment_variables)
        
        # build a response that returns instance id, challenge, and all env vars
        environment_variables["INSTANCE_ID"] = instance_id  # Add instance_id as an environment variable
        print(f"{instance_id} - {challenge} - {environment_variables} - building")
        subprocess.run(["docker-compose", "-f", "instances/" + instance_id + "/docker-compose.yml", "build"], env=environment_variables)
        subprocess.run(["docker-compose", "-f", "instances/" + instance_id + "/docker-compose.yml", "push"], env=environment_variables)
        subprocess.run(["docker", "stack", "deploy", "--compose-file", "instances/" + instance_id + "/docker-compose.yml", instance_id, "--with-registry-auth"], env=environment_variables)

        environment_variables["IP"] = socket.gethostbyname(socket.gethostname())
        response = {
            "instance_id": instance_id,
            "challenge": challenge,
            "details": environment_variables
        }
        print(f"{instance_id} - {challenge} - {environment_variables} - done")
        return response
    except Exception as e:
        error = {"error": str(e)}
        print(f"{instance_id} - {challenge} - {environment_variables} - error - {error}")
        return error
