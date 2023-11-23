import subprocess
import uuid
import os
import shutil
import helper
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
    #generate a random unique network port for the web app
    #port = helper.get_port()
    #environment_variables["PORT"] = str(port)
    if environment_variables is not None:
        print(environment_variables)
        environment_variables = dict(environment_variables)
    print(environment_variables)
    return subprocess.run(["docker-compose", "-f", "instances/" + instance_id + "/docker-compose.yml", "up","-d"], env=environment_variables)