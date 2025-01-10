from flask import Flask
from project_monday.views import app_blueprint

# poetry run flask --app project_monday/app run

app = Flask(__name__)

app.register_blueprint(app_blueprint)

