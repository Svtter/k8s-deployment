import fabric
from conf import loop_on_all_node


def install_apparmor_parser(conn: fabric.Connection):
  conn.sudo("apt-get install apparmor -y")


def main():
  loop_on_all_node(install_apparmor_parser)


if __name__ == "__main__":
  main()
