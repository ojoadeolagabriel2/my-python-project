#!/bin/sh

set -xe

# shellcheck disable=SC2039
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd ./nginx && pwd )"
APP_NAME="${ENV_SERVICE_NAME:-aloeda-nginx}"
APP_NAME="ojoadeolagabriel/${APP_NAME}"
VERSION="1.${2:-$(date +%Y%m%d%H%M%S)}"

# switch to nginx root dir
cd "$DIR"

# build latest image
docker build -t "${APP_NAME}:latest" .
# build versioned image
docker build -t "${APP_NAME}:${VERSION}" .
# push
docker push "${APP_NAME}:latest"

# cleanup
docker system prune -af