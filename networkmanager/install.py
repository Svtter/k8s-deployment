from conf import loop_on_all_node


def install_networkmanager():
  loop_on_all_node(lambda conn: conn.sudo("apt-get install network-manager -y"))


def main():
  install_networkmanager()


if __name__ == "__main__":
  main()
