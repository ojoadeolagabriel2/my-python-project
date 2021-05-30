import os
import logging

__default_k8s_host__ = "localhost"
__default_k8s_host_port__ = 50002
URL_TEMPLATE = "http://{}:{}/pokemon/{}"


def resolve_app_env():
    return "production" if os.environ.__contains__("ENV_IS_PROD_ENV") else "development"


def resolve_app_port():
    if os.environ.__contains__("ENV_APP_PORT"):
        logging.debug("app port found {}".format(int(os.environ["ENV_APP_PORT"])))
        return int(os.environ["ENV_APP_PORT"])
    else:
        logging.debug("found nothing ENV_APP_PORT")
        return 12346


def resolve_pokemon_host():
    if os.environ.__contains__("ENV_POKEMON_SERVICE_HOST"):
        logging.debug("pokemon host env found {}".format(str(os.environ["ENV_POKEMON_SERVICE_HOST"])))
        return str(os.environ["ENV_POKEMON_SERVICE_HOST"])
    else:
        logging.debug("found nothing ENV_POKEMON_SERVICE_HOST")
        return __default_k8s_host__


def resolve_pokemon_host_port():
    if os.environ.__contains__("ENV_POKEMON_SERVICE_HOST_PORT"):
        logging.debug("pokemon host port env found {}".format(str(os.environ["ENV_POKEMON_SERVICE_HOST_PORT"])))
        return str(os.environ["ENV_POKEMON_SERVICE_HOST_PORT"])
    else:
        logging.debug("found nothing ENV_POKEMON_SERVICE_HOST_PORT")
        return __default_k8s_host_port__
