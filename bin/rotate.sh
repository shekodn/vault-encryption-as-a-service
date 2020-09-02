#!/usr/bin/env bash
set -e

APP=api

docker-compose exec --user=vault vault vault write -f transit/keys/${APP}/rotate

