import typing as t

import fabric

master_ip = ["192.168.4.198", "192.168.4.222", "192.168.4.178"]
nodes_ip = ["192.168.4.177", "192.168.4.138", "192.168.4.199"]

config = fabric.Config(
  overrides={
    "sudo": {
      "password": "1223",
    }
  }
)


def get_conn(ip: str) -> fabric.Connection:
  conn = fabric.Connection(ip, user="svtter", config=config)
  return conn


def loop_on_all_node(func: t.Callable[[fabric.Connection], None]):
  for ip in [*master_ip, *nodes_ip]:
    conn = get_conn(ip)
    func(conn)
