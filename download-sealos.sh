#!/bin/bash

# 检查 root 用户
if [ "$EUID" -ne 0 ]; then
  echo "请使用 root 用户执行此脚本"
  exit 1
fi

VERSION=v5.0.1
if [ ! -f "sealos_${VERSION#v}_linux_amd64.tar.gz" ]; then
  wget https://github.com/labring/sealos/releases/download/${VERSION}/sealos_${VERSION#v}_linux_amd64.tar.gz
fi

tar zxvf sealos_${VERSION#v}_linux_amd64.tar.gz sealos && chmod +x sealos && mv sealos /usr/bin
