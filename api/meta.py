from flask import g, abort, request
from flask_restx import Namespace, Resource

from api.context import get_meta

meta_namespace = Namespace("meta", "Metadata retrieval")

class Section(Resource):

    @get_meta
    def get(self, section_name = None):
        pass

    @get_meta
    def post(self):
        pass

class FileMetadata(Resource):
    
    @get_meta
    def get(self, seciton_name = None):
        pass

    @get_meta
    def post(self, section_name):
        pass

class Search(Resource):
    
    @get_meta
    def get(self, section_name = None):
        pass

class Index(Resource):
    
    @get_meta
    def get(self, section_name = None):
        pass