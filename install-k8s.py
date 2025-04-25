#!/bin/bash
import argparse
import os

from conf import master_ip, nodes_ip

parser = argparse.ArgumentParser()
parser.add_argument("--cmd", type=str, default="install", choices=["install", "reset"])
args = parser.parse_args()

cmd = f"""
sealos run registry.cn-shanghai.aliyuncs.com/labring/kubernetes:v1.29.9 \
  registry.cn-shanghai.aliyuncs.com/labring/helm:v3.9.4 \
  registry.cn-shanghai.aliyuncs.com/labring/cilium:v1.13.4 \
  -u root \
  -i /home/svtter/.ssh/id_ed25519 \
  --masters {",".join(master_ip)} \
  --nodes {",".join(nodes_ip)} \
  --debug
"""

if args.cmd == "install":
  print(cmd)
  print("Confirm to install k8s? (y/n)")

  if input() == "y":
    print("Installing k8s...")
    os.system(cmd)
  else:
    print("Installation cancelled")
elif args.cmd == "reset":
  print("Resetting k8s...")
  os.system("sealos reset")
