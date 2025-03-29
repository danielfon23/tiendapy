
from app import db

class Ventas_t(db.Model):
    __tablename__ = 'ventas_t'
    idventa= db.Column(db.Integer, primary_key=True)
    iduser =  db.Column(db.Integer, db.ForeignKey('user.iduser'))
    nro_docu = db.Column(db.String(90), nullable=True)
    fecha = db.Column(db.Date(), nullable=True)
    f_vto = db.Column(db.Date(), nullable=True)
    subtotal = db.Column(db.Float, nullable=True,default=0)
    iva = db.Column(db.Float, nullable=True,default=0)
    descuento = db.Column(db.Float, nullable=True,default=0)
    total = db.Column(db.Float, nullable=True,default=0)
    observacion = db.Column(db.String(300), nullable=True)

    ventas_d = db.relationship("Ventas_d", back_populates="ventas_t")

    def get_id(self):
        return str(self.idventa)
    