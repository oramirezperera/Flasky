from flask import Flask, request, make_response, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)