import fabric

from conf import get_conn, master_ip, nodes_ip


def cp_pass(conn: fabric.Connection):
  conn.sudo("cp ~/.ssh/authorized_keys /root/.ssh/authorized_keys")


def cp_pass_for_all_servers():
  for ip in master_ip:
    cp_pass(get_conn(ip))

  for ip in nodes_ip:
    cp_pass(get_conn(ip))


if __name__ == "__main__":
  cp_pass_for_all_servers()
