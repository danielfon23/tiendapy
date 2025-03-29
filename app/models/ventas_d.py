
from app import db

class Ventas_d(db.Model):
    __tablename__ = 'ventas_d'
    iddetalle = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idventa = db.Column(db.Integer, db.ForeignKey('ventas_t.idventa'))
    idproducto =  db.Column(db.Integer, db.ForeignKey('producto.idproducto'))
    nro_docu = db.Column(db.String(90), nullable=True)
    fecha = db.Column(db.Date(), nullable=True)
    precio = db.Column(db.Float, nullable=False,default=0)
    cantidad = db.Column(db.Integer, nullable=False,default=1)
    iva = db.Column(db.Integer, nullable=True,default=0)
    descuento = db.Column(db.Float, nullable=True,default=0)
    total = db.Column(db.Float, nullable=True,default=0)

    productos = db.relationship('Productos',back_populates="ventas_d")
    ventas_t = db.relationship("Ventas_t", back_populates="ventas_d")