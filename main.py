"""change hostname of given hostname"""

import json

import fabric

from conf import get_conn, loop_on_all_node, master_ip, nodes_ip


def set_hostnames():
  # set master hostname
  cnt = 1
  res = []

  for ip in master_ip:
    hostname = f"master-{cnt}.lan"
    change_hostname(get_conn(ip), hostname)
    cnt += 1
    res.append(f"{hostname} {ip}")

  # set node hostname
  cnt = 1
  for ip in nodes_ip:
    hostname = f"node-{cnt}.lan"
    change_hostname(get_conn(ip), hostname)
    cnt += 1
    res.append(f"{hostname} {ip}")

  with open("name.json", "w") as f:
    json.dump({"servers": res}, f)
  return res


def change_hostname(conn: fabric.Connection, hostname: str):
  """change hostname of given hostname"""
  conn.sudo(f"hostnamectl set-hostname {hostname}")


def sync_time(conn: fabric.Connection):
  """sync time"""
  # 检查两个包是否都已安装
  timesyncd_installed = conn.run(
    "dpkg -l | grep -q '^ii.*systemd-timesyncd '", warn=True
  ).ok

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
  loop_on_all_node(sync_time)


def show_time(conn: fabric.Connection):
  """show time"""
  conn.run("date")


def show_all_time():
  """show time for all servers"""
  loop_on_all_node(show_time)


if __name__ == "__main__":
  # set_hostnames()
  # sync_all_time()
  show_all_time()
