from flask import Flask
from flask_restx import Api

from asgard_sdk.models.config_pb2 import ServerConfig

from api.meta import meta_namespace # try this in container
from api.context import teardown_meta

class Rest(object):
    def __init__(self, config: ServerConfig):
        self.__config = config

        self.__app = Flask(__name__)
        self.__api = Api(app=self.__app, doc="/docs")

        self.__app.config["config"] = self.__config
    
    def get_config(self):
        return self.__config

    def __build_namespaces(self):
        self.__api.add_namespace(meta_namespace, path="/meta")

    def __register_teardowns(self):
        self.__app.teardown_appcontext(teardown_meta)
    
    def run(self):
        self.__register_teardowns()
        self.__build_namespaces()

        self.__app.run(port=80, debug=True)