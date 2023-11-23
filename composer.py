import subprocess
import uuid
import os
import shutil
def spawn_challenge(challenge, environment_variables=None):
    """
    Spawn a new instance of a challenge.
    :param challenge: provide the name of the docker-compose file for the challenge"
    :param environment_variables: provide the environment variables for the docker-compose file as dictionary.
    :return: output of detached compose command
    """
    instance_id = str(uuid.uuid4())
    path_to_compose_file = "challenges/" + challenge
    #copy compose file to instance folder
    os.makedirs("instances/" + instance_id)
    shutil.copy(path_to_compose_file, "instances/" + instance_id + "/docker-compose.yml")

    #create instance network
    #subprocess.run(["docker", "network", "create", instance_id])

    return subprocess.run(["docker-compose", "-f", "instances/" + instance_id + "/docker-compose.yml", "up","-d"], env=environment_variables)