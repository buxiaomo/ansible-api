from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@mysql:3306/ansible-api'
db = SQLAlchemy(app)

class PlayBook(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(PlayBook, '/')


if __name__ == '__main__':
    app.run()
