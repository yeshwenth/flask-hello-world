import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, ClientsideFunction,State

import numpy as np
import pandas as pd
import os
import cv2
import keras
import tensorflow as tf

import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
