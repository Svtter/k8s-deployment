from conf import get_conn, master_ip, nodes_ip


def check_mac_address():
  for ip in [*master_ip, *nodes_ip]:
    conn = get_conn(ip)
    print(f"ip: {ip}")
    conn.run("ip link | grep -E 'ens|eth' | awk '{print $2}'")
    print('-'*32)


def check_product_uuid():
  for ip in [*master_ip, *nodes_ip]:
    conn = get_conn(ip)
    conn.sudo("cat /sys/class/dmi/id/product_uuid")


if __name__ == "__main__":
  check_mac_address()
  check_product_uuid()
