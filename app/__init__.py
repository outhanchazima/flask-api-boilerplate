from app.src.models import UserModel
from app.src import app, db

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate


from flask_restx import Api
from flask import Blueprint

from app.src.controller.userAuth import api as userNS
from app.src.controller.userAuth import api2 as authNS

blueprint = Blueprint('api', __name__)

apiDocsAuthorization = {
    'Basic Auth': {
        'type': 'basic',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          version="1.0",
          title="Started API",
          description="What api does",
          authorizations=apiDocsAuthorization,
          security='Bearer Auth'
          )

api.add_namespace(userNS, path='/users')
api.add_namespace(authNS)

migrate = Migrate(app, db)