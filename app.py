from flask import Flask, app

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Welcome to home page'