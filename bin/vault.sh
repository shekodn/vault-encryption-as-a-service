#!/usr/bin/env bash
set -e

APP=api

docker-compose exec --user=vault vault vault secrets enable transit
docker-compose exec --user=vault vault vault token create -period=24h
docker-compose exec --user=vault vault vault write -force transit/keys/${APP}

