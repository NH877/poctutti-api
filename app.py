from flask import Flask, jsonify
import json
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

# Init application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aqvwfwcpystbgx:b601a0d01f4cb762589fddc802021c578e46308fb822cd5d6523f785a806fef7@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d7dm2us6j1gssm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init database
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    amount = db.Column(db.Integer)
    image = db.Column(db.String(500))
    active = db.Column(db.Boolean)

    def __init__(self, name, amount, image, active):
        self.name = name
        self.amount = amount
        self.image = image
        self.active = active

# Product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('product_id', 'name', 'amount', 'image', 'active')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/')
def index():
    product_list = Product.query.all()
    result = products_schema.dump(product_list)
    return jsonify(result)

app.run()