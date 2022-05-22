from db.database import db, ma

class Store(db.Model):
    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store

# Init schemas
store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)