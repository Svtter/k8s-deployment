"""change hostname of given hostname"""

import fabric


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


def set_hostnames():
  master_ip = ["192.168.4.198", "192.168.4.222", "192.168.4.177"]
  nodes_ip = ["192.168.4.103", "192.168.4.138", "192.168.4.199"]

  # set master hostname
  cnt = 1
  for ip in master_ip:
    hostname = f"master-{cnt}"
    change_hostname(get_conn(ip), hostname)
    cnt += 1

  # set node hostname
  cnt = 1
  for ip in nodes_ip:
    hostname = f"node-{cnt}"
    change_hostname(get_conn(ip), hostname)
    cnt += 1


def change_hostname(conn: fabric.Connection, hostname: str):
  """change hostname of given hostname"""
  conn.sudo(f"hostnamectl set-hostname {hostname}")


def sync_time(conn: fabric.Connection):
  """sync time"""
  # 检查两个包是否都已安装
  timesyncd_installed = conn.run("dpkg -l | grep -q '^ii.*systemd-timesyncd '", warn=True).ok

  # 如果任一包未安装，则更新并安装
  if not timesyncd_installed:
    conn.sudo("apt-get update")
    conn.sudo("apt-get install -y systemd-timesyncd")

  # 启用并启动 timesyncd 服务
  conn.sudo("systemctl enable systemd-timesyncd")
  conn.sudo("systemctl start systemd-timesyncd")

  # 设置时区
  conn.sudo("timedatectl set-timezone Asia/Shanghai")
  conn.sudo("timedatectl set-ntp true")


def sync_all_time():
  """sync time for all servers"""
  master_ip = ["192.168.4.198", "192.168.4.222", "192.168.4.177"]
  nodes_ip = ["192.168.4.103", "192.168.4.138", "192.168.4.199"]

  for ip in master_ip:
    sync_time(get_conn(ip))

  for ip in nodes_ip:
    sync_time(get_conn(ip))


if __name__ == "__main__":
  # set_hostnames()
  sync_all_time()
