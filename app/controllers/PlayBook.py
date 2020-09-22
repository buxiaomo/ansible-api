from flask_restful import Resource


class PlayBookAPI(Resource):

    def get(self):
        return {'hello': 'world'}
