from flask import Flask, request, make_response, render_template
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', 
                            current_time = datetime.utcnow())



@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)