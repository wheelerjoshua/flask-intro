from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice')
def roll_dice():
    numbers = list(np.random.randint(1,7,size = 3).astype(str))
    return render_template('roll-dice.html', dice_roll = numbers)

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting-result.html', greeting=greeting)