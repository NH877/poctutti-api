from __main__ import app, request
from db.database import db
from models.product import Product, products_schema, product_schema

ROUTE = '/product'
ROUTE_ID = '/product/<id>'

# Get All
@app.route(ROUTE, methods=['GET'])
def get_all():
    product_list = Product.query.all()
    return products_schema.jsonify(product_list)

# Get
@app.route(ROUTE_ID, methods=['GET'])
def get(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Add
@app.route(ROUTE, methods=['POST'])
def add():
    name = request.json['name']
    amount = request.json['amount']
    image = request.json['image']
    active = request.json['active']

    product = Product(name, amount, image, active)
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product)

# Update
@app.route(ROUTE_ID, methods=['PUT'])
def update(id):
    product = Product.query.get(id)

    name = request.json['name']
    amount = request.json['amount']
    image = request.json['image']
    active = request.json['active']

    product.name = name
    product.amount = amount
    product.image = image
    product.active = active

    db.session.commit()
    return product_schema.jsonify(product)

# Delete
@app.route(ROUTE_ID, methods=['DELETE'])
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)