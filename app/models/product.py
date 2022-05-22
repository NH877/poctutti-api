from db.database import db, ma

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    amount = db.Column(db.Integer)
    price = db.Column(db.Float)
    image = db.Column(db.String(500))
    active = db.Column(db.Boolean)

    def __init__(self, name, amount, price, image, active):
        self.name = name
        self.amount = amount
        self.price = price
        self.image = image
        self.active = active

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

# Init schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)