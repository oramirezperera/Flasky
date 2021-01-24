from flask import Flask, request, make_response
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'



@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello {name}!</h1>'