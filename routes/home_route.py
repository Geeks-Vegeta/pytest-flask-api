from flask_restful import Resource
import json
from controllers.home_controller import home


class HomeRoute(Resource):
    
    def get(self):
        return home()