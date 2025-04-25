import fabric
from conf import loop_on_all_node


def config_conflict(conn: fabric.Connection):
  conn.sudo("mkdir -p /etc/NetworkManager/conf.d")
  conn.put("networkmanager/rke2-canal.conf", "/tmp/rke2-canal.conf")
  conn.sudo("mv /tmp/rke2-canal.conf /etc/NetworkManager/conf.d/rke2-canal.conf")
  conn.sudo("systemctl restart NetworkManager")

def main():
  loop_on_all_node(config_conflict)


if __name__ == "__main__":
  main()
