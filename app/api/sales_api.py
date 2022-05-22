from __main__ import app, request
from db.database import db
from models.sale import Sale, sale_schema, sales_schema
from sqlalchemy.orm import joinedload

ROUTE = '/sale'
ROUTE_ID = '/sale/<id>'

# Get All
@app.route(ROUTE, methods=['GET'])
def get_all_sales():
    sale_list = Sale.query.options(joinedload('store'))
    return sales_schema.jsonify(sale_list)

# Get
@app.route(ROUTE_ID, methods=['GET'])
def get_sale(id):
    sale = Sale.query.get(id)
    return sale_schema.jsonify(sale)

# Add
@app.route(ROUTE, methods=['POST'])
def add_sale():
    store_id = request.json['store_id']

    sale = Sale(store_id)
    db.session.add(sale)
    db.session.commit()
    return sale_schema.jsonify(sale)

# Update
@app.route(ROUTE_ID, methods=['PUT'])
def update_sale(id):
    sale = Sale.query.get(id)

    store_id = request.json['store_id']

    sale.store_id = store_id

    db.session.commit()
    return sale_schema.jsonify(sale)

# Delete
@app.route(ROUTE_ID, methods=['DELETE'])
def delete_sale(id):
    sale = Sale.query.get(id)
    db.session.delete(sale)
    db.session.commit()
    return sale_schema.jsonify(sale)