from flask_project.app.app import app
from flask import render_template, jsonify, request
from db_service import DbService

db = DbService()

@app.route('/')
def index():
    my_name = 'Alexey'
    return render_template('index.html', name=my_name)

@app.route('/products', methods=['GET'])
def products():
    products = db.get_products()
    return jsonify(eqtls=[p.serialize() for p in products])

@app.route('/products/<string:sku>', methods=['GET'])
def products(sku):
    product = db.get_product(sku)
    if not product:
        return abort(404)
    else:
        return jsonify(eqtls=product)

@app.route('/products/<string:sku>', methods=['DELETE'])
def products(sku):
    product = db.delete_product(sku)
    if not product:
        return abort(404)
    else:
        return jsonify('OK')

@app.route('/products/<string:sku>', methods=['PUT'])
def update_products_post(sku):
    if not sku:
        return abort(400)
    product = parse_request(request)
    db.add_product(product)

@app.route('/products', methods=['POST'])
def add_products_post():
    if not request.form:
        return abort(400)

    product = parse_request(request)
    db.add_product(product)
    return jsonify({'product': product.serialize()})

def parse_request(request):
    p = ProductCreator().Create(request.form.get('type_product'))
    p.sku = request.form.get('sku')
    p.name = request.form.get('name')
    p.qty = request.form.get('qty')
    p.manufacter = request.form.get('manufacter')
    p.price = request.form.get('price')
    return p