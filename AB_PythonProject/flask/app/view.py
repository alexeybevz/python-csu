from app import app
from flask import render_template

@app.route('/')
def index():
    my_name = 'Alexey'
    return render_template('index.html', name=my_name)