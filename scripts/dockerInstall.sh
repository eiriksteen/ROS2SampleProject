#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
BLANK='\033[0m'
sudo apt-get -y install curl
sudo apt-get remove docker docker-engine docker.io containerd runc
echo  "${GREEN} Getting ready to install Docker, Cho Chooo! ${BLANK}"
sudo apt-get -y install sl
sl
sudo -E apt-get -y install apt-transport-https ca-certificates software-properties-common && \
curl -sL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \
arch=$(dpkg --print-architecture) && \
sudo -E add-apt-repository "deb [arch=${arch}] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
sudo -E apt-get update && \
sudo -E apt-get -y install docker-ce docker-compose

echo  " ${GREEN} Testing Docker ${BLANK}"
sudo docker run hello-world
sudo docker run docker/whalesay cowsay Docker Installed Successfully
sudo systemctl daemon-reload
sudo systemctl restart docker

