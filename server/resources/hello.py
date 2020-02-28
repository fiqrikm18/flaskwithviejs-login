from flask_restful import Resource

class HelloResource(Resource):
    def get(self, id=None):
        if not id:
            return {'message': 'Hello, world!'}
        
        return {'message': 'Hello, world!', 'id': id}