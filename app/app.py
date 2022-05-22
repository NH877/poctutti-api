from flask import Flask, jsonify
from db.database import db, ma
from config import BaseConfig
from models.product import Product, products_schema

# Init application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = BaseConfig.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = BaseConfig.DATABASE_TRACK_MODIFICATIONS

# Init database
db.init_app(app)
ma.init_app(app)

@app.route('/')
def index():
    product_list = Product.query.all()
    result = products_schema.dump(product_list)
    return jsonify(result)

app.run()