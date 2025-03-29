from flask_login import UserMixin
from app import db

class Productos(db.Model, UserMixin):
    __tablename__ = 'producto'
    idproducto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False,default=0)
    descripcion = db.Column(db.String(300), nullable=True)
    img1 = db.Column(db.String(300), nullable=True)
    img2 = db.Column(db.String(300), nullable=True)
    img3 = db.Column(db.String(300), nullable=True)
    img4 = db.Column(db.String(300), nullable=True)
    idcategoria = db.Column(db.Integer, db.ForeignKey('categoria.idcategoria'))
    
    carrito = db.relationship('Carrito',back_populates="productos")
    ventas_d = db.relationship('Ventas_d',back_populates="productos")
    
    categoria = db.relationship("Categorias", back_populates = "productos")
    def get_id(self):
        return str(self.idproducto)
    
    def get_img(self, img_attr):
        return getattr(self, img_attr) if getattr(self, img_attr) else "productos.png"
    