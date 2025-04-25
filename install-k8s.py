#!/bin/bash
import os

from conf import master_ip, nodes_ip

cmd = f"""
sealos run registry.cn-shanghai.aliyuncs.com/labring/kubernetes:v1.29.9 registry.cn-shanghai.aliyuncs.com/labring/helm:v3.9.4 registry.cn-shanghai.aliyuncs.com/labring/cilium:v1.13.4 \
     --user svtter \
     --passwd 1223 \
     --masters {",".join(master_ip)} \
     --nodes {",".join(nodes_ip)}
"""

print(cmd)
print("Confirm to install k8s? (y/n)")

if input() == "y":
  print("Installing k8s...")
  os.system(cmd)
else:
  print("Installation cancelled")
