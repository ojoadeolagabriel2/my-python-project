#!/bin/sh

set -xe

# shellcheck disable=SC2039
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd .. && pwd )"
SERVICE_NAME="${ENV_SERVICE_NAME:-my-py-app}"
IMAGE_NAME="ojoadeolagabriel/${SERVICE_NAME}"
VERSION="1.${2:-$(date +%Y%m%d%H%M%S)}"

# switch to project root dir
cd "$DIR"

# build latest image
docker build -t "${IMAGE_NAME}:latest" .
# build versioned image
docker build -t "${IMAGE_NAME}:${VERSION}" .
# push
docker push "${IMAGE_NAME}:latest"

# cleanup
docker system prune -af