import subprocess
def spawn_challenge(challenge, environment_variables=None):
    """
    Spawn a new instance of a challenge.
    :param challenge: provide the name of the docker-compose file for the challenge"
    :param environment_variables: provide the environment variables for the docker-compose file as dictionary.
    :return: output of detached compose command
    """
    path_to_compose_file = "challenges/" + challenge
    return subprocess.run(["docker-compose", "-f", path_to_compose_file, "up","-d"], env=environment_variables)