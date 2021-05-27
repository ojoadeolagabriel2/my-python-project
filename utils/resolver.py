import os

__default_k8s_host__ = "pokemon-information-service-service.information-ns.svc.cluster.local"
__default_host__ = "localhost"


def resolve_pokemon_host():
    if os.environ.__contains__("ENV_POKEMON_SERVICE_HOST"):
        return str(os.environ["ENV_POKEMON_SERVICE_HOST"])
    else:
        return __default_k8s_host__
