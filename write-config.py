import json
import os

from conf import get_conn

with open("./name.json", "r") as f:
  data = json.load(f)


host_template = """
Host {hostname}
  HostName {ip}
  User root
  IdentityFile ~/.ssh/id_ed25519
"""


def build_config(hostname, ip):
  return host_template.format(hostname=hostname, ip=ip)


with open(os.path.expanduser("~/.ssh/config"), "w") as f:
  for server in data["servers"]:
    hostname, ip = server.split(" ")

    f.write(build_config(hostname, ip) + "\n")
