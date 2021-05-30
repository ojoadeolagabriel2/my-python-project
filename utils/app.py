import logging
from utils.resolver import *
from flask import Flask

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')


class AppContext:
    """api default client"""
    app = Flask(__name__)
    app_ready = False

    def __init__(self, ):
        if not AppContext.app_ready:
            AppContext.app.config['JSON_SORT_KEYS'] = False
            AppContext.app.config['FLASK_ENV'] = resolve_app_env()
            AppContext.app_ready = True
            logging.info(f"created context")
