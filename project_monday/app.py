from flask import Flask
from project_monday.views import app_blueprint

app = Flask(__name__)

app.register_blueprint(app_blueprint)
