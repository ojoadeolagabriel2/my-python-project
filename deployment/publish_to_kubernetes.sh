#!/bin/sh

set -xe

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

kubectl delete namespace py-ns || :
kubectl apply -f "${DIR}/apply.yml"