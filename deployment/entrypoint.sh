#!/bin/sh

set -ex

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
DOCKER_ACCESS_TOKEN="${ENV_DOCKER_ACCESS_TOKEN:-b94a013c-eb16-4c14-96dd-23bfc40d2b1e}"
DOCKER_USERNAME="${ENV_DOCKER_USERNAME:-ojoadeolagabriel}"

# prepare docker
echo "${DOCKER_ACCESS_TOKEN}" | docker login --username "${DOCKER_USERNAME}" --password-stdin

"${DIR}"/build_nginx_publish_to_docker.sh
"${DIR}"/build_publish_to_docker.sh
"${DIR}"/publish_to_kubernetes.sh