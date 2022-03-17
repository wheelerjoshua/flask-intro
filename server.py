from flask import Flask
import numpy as np
import random
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll_dice')
def roll_dice():
    numbers = np.random.randint(1,7, dtype = str, size = 3)
    return print(f'Your numbers are {[number for number in numbers]}')