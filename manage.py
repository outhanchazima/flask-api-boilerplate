from flask.cli import FlaskGroup
from flask_cors import CORS

from app.src.utils import logging
from app import api, app, db, blueprint

logger = logging.GetLogger(__name__)    

# ORiginal stuff begins here

app.register_blueprint(blueprint)

app.app_context().push()

cli = FlaskGroup(app)



if __name__ == '__main__':
    cli()