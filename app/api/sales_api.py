from __main__ import app, request
from viewmodels.product_vm import ProductVM
from viewmodels.store_vm import StoreVM
from viewmodels.sale_vm import SaleVM
from db.database import db
from models.sale import Sale, sale_schema, sales_schema
from models.product_sale import ProductSale, product_sale_schema, products_sales_schema
from sqlalchemy.orm import joinedload
from flask import Response
import json

ROUTE = '/sale'
ROUTE_ID = '/sale/<id>'

# Get All -- Not mapped for a good and understandable viewmodel
@app.route(ROUTE, methods=['GET'])
def get_all_sales():
    prod_sale_list = ProductSale.query.options(joinedload('sale'))
    return products_sales_schema.jsonify(prod_sale_list)

# Get -- Mapped to a cool viewmodel
@app.route(ROUTE_ID, methods=['GET'])
def get_sale(id):
    prod_sale_list = ProductSale.query.filter_by(sale_id=id).all()

    # Create Products
    products = []

    for prod_sale in prod_sale_list:
        prod_vm = ProductVM(prod_sale.product.product_id, prod_sale.product.name, prod_sale.product.price, prod_sale.quantity)
        products.append(prod_vm)

    prod_sale_first = prod_sale_list[0]

    # Create StoreVM
    store_vm = StoreVM(prod_sale_first.sale.store.store_id, prod_sale_first.sale.store.name)

    # Create SaleVM
    sale_vm = SaleVM(prod_sale_first.sale.sale_id, prod_sale_first.sale.time.strftime("%d-%m-%Y %H:%M:%S"), store_vm, products)

    # Set response (Since here we're not using schemas)
    response = Response(json.dumps(sale_vm, default=lambda o: o.__dict__))
    response.headers['Content-Type'] = 'application/json'

    return response

# Add
@app.route(ROUTE, methods=['POST'])
def add_sale():
    # Create Sale
    store_id = request.json['store_id']
    sale = Sale(store_id)
    db.session.add(sale)
    db.session.commit()

    # Create ProductSale
    product_sale_list = []
    for product in request.json['products']:
        product_sale = ProductSale(sale.sale_id, product['product_id'], product['quantity'])
        product_sale_list.append(product_sale)

    # Save ProductSale
    db.session.bulk_save_objects(product_sale_list)
    db.session.commit()

    return sale_schema.jsonify(sale)