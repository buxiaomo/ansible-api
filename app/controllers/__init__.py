from flask import Blueprint
from flask_restful import Api
from app.controllers.PlayBook import PlayBookAPI


main = Blueprint('main', __name__)

api = Api(main)


api.add_resource(PlayBookAPI, '/index')