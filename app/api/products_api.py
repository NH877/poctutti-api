from __main__ import app
from flask import jsonify
from models.product import Product, products_schema

@app.route('/')
def index():
    product_list = Product.query.all()
    result = products_schema.dump(product_list)
    return jsonify(result)