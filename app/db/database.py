from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow

# Init database
db = SQLAlchemy()
# Init Marshmallow
ma = Marshmallow()