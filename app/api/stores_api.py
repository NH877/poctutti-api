from app import app, request
from db.database import db
from models.store import Store, stores_schema, store_schema

ROUTE = '/store'
ROUTE_ID = '/store/<id>'

# Get All
@app.route(ROUTE, methods=['GET'])
def get_all_stores():
    store_list = Store.query.all()
    return stores_schema.jsonify(store_list)

# Get
@app.route(ROUTE_ID, methods=['GET'])
def get_store(id):
    store = Store.query.get(id)
    return store_schema.jsonify(store)

# Add
@app.route(ROUTE, methods=['POST'])
def add_store():
    name = request.json['name']

    store = Store(name)
    db.session.add(store)
    db.session.commit()
    return store_schema.jsonify(store)

# Update
@app.route(ROUTE_ID, methods=['PUT'])
def update_store(id):
    store = Store.query.get(id)

    name = request.json['name']

    store.name = name

    db.session.commit()
    return store_schema.jsonify(store)

# Delete
@app.route(ROUTE_ID, methods=['DELETE'])
def delete_store(id):
    store = Store.query.get(id)
    db.session.delete(store)
    db.session.commit()
    return store_schema.jsonify(store)