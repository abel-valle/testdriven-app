# services/users/project/__init__.py

import os
import sys
from flask import Flask, jsonify
from flask_restful import Resource, Api

# instantiate the app
app = Flask(__name__)
# print(app.config, file=sys.stderr)
api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# set config
app.config.from_object('project.config.DevelopmentConfig') # new

class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(UsersPing, '/users/ping')

