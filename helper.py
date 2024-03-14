import random
#generate a random unique network port for the web app
used_ports = []
def get_port():
    """
    Generate a random port for the web app.
    :return: port number
    """
    port = random.randint(49152, 65535)
    while port in used_ports:
        port = random.randint(49152, 65535)
    used_ports.append(port)
    return str(port)
