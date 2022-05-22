from models.product import ProductSchema
from models.sale import SaleSchema
from db.database import db, ma

class ProductSale(db.Model):
    product_sale_id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.sale_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Integer)
    sale = db.relationship('Sale', backref='products_sales')
    product = db.relationship('Product', backref='products_sales')

    def __init__(self, sale_id, product_id, quantity):
        self.sale_id = sale_id
        self.product_id = product_id
        self.quantity = quantity

class ProductSaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductSale
    
    sale = ma.Nested(SaleSchema)
    product = ma.Nested(ProductSchema)

# Init schemas
product_sale_schema = ProductSaleSchema()
products_sales_schema = ProductSaleSchema(many=True)