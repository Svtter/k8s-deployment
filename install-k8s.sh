#!/bin/bash


sealos run registry.cn-shanghai.aliyuncs.com/labring/kubernetes:v1.29.9 registry.cn-shanghai.aliyuncs.com/labring/helm:v3.9.4 registry.cn-shanghai.aliyuncs.com/labring/cilium:v1.13.4 \
     --user svtter \
     --passwd 1223 \
     --masters 192.168.4.198,192.168.4.222,192.168.4.177 \
     --nodes 192.168.4.103,192.168.4.138,192.168.4.199
