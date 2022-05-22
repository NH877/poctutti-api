from db.database import db, ma

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

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('product_id', 'name', 'amount', 'image', 'active')

# Init schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)