from flask import Blueprint, render_template

app_blueprint = Blueprint('index', __name__, template_folder='templates')


@app_blueprint.route('/')
def index():
    return render_template('index.html')
