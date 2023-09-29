import subprocess
def spawn_container(path_to_compose_file):
    subprocess.run(["docker-compose", "-f", path_to_compose_file, "up","-d"])