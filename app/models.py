from . import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)  # Float → Numeric(10,2) に変更

    def __repr__(self):
        return f'<Product id={self.id}, name={self.name}, price={self.price}>'
