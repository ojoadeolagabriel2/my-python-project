#!/bin/sh

set -ex

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

"${DIR}"/build_publish_to_docker.sh
"${DIR}"/publish_to_kubernetes.sh