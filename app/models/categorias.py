from app import db

class Categorias(db.Model):
    __tablename__ = 'categoria'
    idcategoria= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    img1 = db.Column(db.String(300), nullable=True)

    productos = db.relationship("Productos", back_populates="categoria")

    def get_id(self):
        return str(self.idcategoria)
    
    def get_img(self, img_attr):
        return getattr(self, img_attr) if getattr(self, img_attr) else "usuario.gif"