from flask import Blueprint, render_template

app_blueprint = Blueprint('index', __name__, template_folder='templates')


@app_blueprint.route('/')
def index():
    return render_template('index.html')


@app_blueprint.route('/random', methods=['GET', 'POST'])
def randomizer():

    import random
    import time

    time.sleep(.2)

    return render_template('randomizer.html', r=int(random.random() * 100))
