from flask import Flask
from .routes.routes_activity import activityBluePrint
from .routes.routes_auth import authBluePrint
from .routes.routes_profile import profileBluePrint
from .routes.routes_project import projectBluePrint
from .routes.routes_skill import skillBluePrint


app = Flask(__name__,
  static_url_path='', 
  static_folder='./view',
  template_folder='./view'
)

app.secret_key = 'asdfsadfasf'
app.register_blueprint(activityBluePrint)
app.register_blueprint(authBluePrint)
app.register_blueprint(profileBluePrint)
app.register_blueprint(projectBluePrint)
app.register_blueprint(skillBluePrint)

from . import cors

from .routes import routes_index
