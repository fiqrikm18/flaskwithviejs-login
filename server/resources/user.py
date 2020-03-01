from flask_restful import Resource
from models.models import UserModel, UserSchema, db
from flask import request
from libs.utils import Utils


users_schema = UserSchema(many=True)
user_schema = UserSchema()


class UserResource(Resource):
    def get(self, userid=None):
        if userid:
            data = UserModel.find_by_id(id=userid)
            return {'status': 'success', 'user_data': data}

        data = UserModel.find_all()
        return {'data': data}

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'No data input provided'}

        # TODO: add checking username existed

        user = UserModel(
            username = json_data['username'],
            password= Utils.encrypt_pass(json_data['password'])
        )

        user.add()
        res = user_schema.dump(user)

        return {'result': res}

    def delete(self, userid):
        return {'user_id': userid}
