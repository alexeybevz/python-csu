from flask_project.app.app import app
from flask import render_template, jsonify
from db_service import DbService

db = DbService()

@app.route('/')
def index():
    my_name = 'Alexey'
    return render_template('index.html', name=my_name)

@app.route('/products')
def products():
    products = db.get_products()
    return jsonify(eqtls=[p.serialize() for p in products])