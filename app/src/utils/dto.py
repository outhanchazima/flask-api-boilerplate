from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'phoneNo': fields.String(required=True, description='user phone number'),
        'username': fields.String(required=True, description='user username'),
        # 'password': fields.String(required=True, description='user password'),
        'userId': fields.Integer(required=True, description="user id")

    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    auth = api.model('auth', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })