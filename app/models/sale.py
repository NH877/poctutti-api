from models.store import StoreSchema
from db.database import db, ma
from datetime import datetime

class Sale(db.Model):
    sale_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'))
    time = db.Column(db.DateTime, default=datetime.now)
    store = db.relationship('Store', backref='sales')

    def __init__(self, store_id):
        self.store_id = store_id

class SaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sale
        
    store = ma.Nested(StoreSchema)

# Init schemas
sale_schema = SaleSchema()
sales_schema = SaleSchema(many=True)