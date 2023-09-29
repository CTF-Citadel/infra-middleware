import subprocess
def spawn_container(challenge):
    path_to_compose_file = "challenges/" + challenge
    subprocess.run(["docker-compose", "-f", path_to_compose_file, "up","-d"])