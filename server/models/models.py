from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

marshmallow = Marshmallow()
db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    join_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserSchema(marshmallow.Schema):
    id = fields.Integer()
    username = fields.String(required=True, error_messages={
                             'required': 'Username cannot be empty'})
    password = fields.String(required=True, error_messages={
                             'required': 'Password cannot be empty'})
    join_date = fields.DateTime()
