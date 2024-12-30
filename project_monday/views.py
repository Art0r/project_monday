from flask import Blueprint

app_blueprint = Blueprint('index', __name__, template_folder='templates')


@app_blueprint.route('/')
def index():
    return 'hello world'
