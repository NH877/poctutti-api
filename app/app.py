from flask import Flask, request
from db.database import db, ma
from config import BaseConfig
from flask_cors import CORS

# Init application
app = Flask(__name__)

# Init CORS
CORS(app, origins=['*'])

# Init database
app.config['SQLALCHEMY_DATABASE_URI'] = BaseConfig.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = BaseConfig.DATABASE_TRACK_MODIFICATIONS
db.init_app(app)
ma.init_app(app)

# Init endpoints
import api.products_api
import api.stores_api
import api.sales_api