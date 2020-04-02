import numpy as np
import pandas as pd
import os
import cv2
import keras
import tensorflow as tf
from flask import jsonify

import base64

app = Flask(__name__)

 
@app.route('/')
def hello_world():
    return 'Hello, Ramji!'
