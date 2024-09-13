#!/usr/bin/env bash

export IMAGE=$1
export DOCKER_USER=$2
export DOCKER_PWD=$3

echo "$DOCKER_PWD" | docker login -u "$DOCKER_USER" --password-stdin
docker-compose -f /home/ec2-user/docker-compose.yml up -d
echo "success"