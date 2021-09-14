#!/bin/bash

RED='\e[0;31m'
GREEN='\e[0;32m'
BLANK='\e[0m'
sudo apt-get -y install curl
sudo apt-get -y install gcc
sudo apt-get remove docker docker-engine docker.io containerd runc
echo  -e "${GREEN} Getting ready to install Docker, Cho Chooo! ${BLANK}"
sudo apt-get -y install sl
sl
sudo -E apt-get -y install apt-transport-https ca-certificates software-properties-common && \
curl -sL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \
arch=$(dpkg --print-architecture) && \
sudo -E add-apt-repository "deb [arch=${arch}] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
sudo -E apt-get update && \
sudo -E apt-get -y install docker-ce docker-compose

echo  -e " ${GREEN} Testing Docker ${BLANK}"
sudo docker run hello-world

echo  -e "${GREEN} Setting up rootless docker ${BLANK}"
sudo apt-get install uidmap
dockerd-rootless-setuptool.sh install
sudo apt-get install -y docker-ce-rootless-extras

#Add to path
BINARY_PATH= "export PATH=/usr/bin:$PATH"
if ! grep -qF "$BINARY_PATH" ~/.bashrc; then echo "$BINARY_PATH" >> ~/.bashrc ; source ~/.bashrc ; fi
SET_DOCKER_HOST="export DOCKER_HOST=unix:///run/user/1000/docker.sock"
if ! grep -qF "$SET_DOCKER_HOST" ~/.bashrc; then echo "$SET_DOCKER_HOST" >> ~/.bashrc ; source ~/.bashrc ; fi

echo  -e "${GREEN} Testing rootless docker ${BLANK}"
systemctl --user start docker
systemctl --user enable docker
