from flask_restful import Resource
from models.models import UserModel, UserSchema


class UserResource(Resource):
    def get(self, userid=None):
        if userid:
            return {'user_id': userid}

        return {'message': 'Hello user message'}

    def post(self):
        # TODO: add logical here
        pass

    def delete(self, userid):
        return {'user_id': userid}
