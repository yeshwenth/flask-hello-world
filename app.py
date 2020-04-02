from flask import Flask
import keras
import tensorflow as tf
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
