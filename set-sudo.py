from fabric import Connection

from conf import get_conn, master_ip, nodes_ip


def set_sudo(conn: Connection):
  conn.run("su -", pty=True)


def set_sudo_for_all_servers():
  for ip in master_ip:
    set_sudo(get_conn(ip))

  for ip in nodes_ip:
    set_sudo(get_conn(ip))


if __name__ == "__main__":
  set_sudo_for_all_servers()
  # reboot_all_servers()
