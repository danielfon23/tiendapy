
from app import db

class Carrito(db.Model):
    __tablename__ = 'carrito'
    idcarrito= db.Column(db.Integer, primary_key=True)
    idproducto = db.Column(db.Integer, db.ForeignKey('producto.idproducto'))
    iduser =  db.Column(db.Integer, db.ForeignKey('user.iduser'))
    cantidad = db.Column(db.Integer, nullable=True, default = 1)

    productos = db.relationship('Productos',back_populates="carrito")
    
    def get_id(self):
        return str(self.idcarrito)
    
    def get_img(self, img_attr):
        return getattr(self, img_attr) if getattr(self, img_attr) else "carrito.png"