from flask_login import UserMixin
from app import db

class Users(db.Model, UserMixin):
    __tablename__ = 'user'
    iduser = db.Column(db.Integer, primary_key=True)
    nameuser = db.Column(db.String(90), unique=True, nullable=False)
    passworduser = db.Column(db.String(300), nullable=False)
    nombre = db.Column(db.String(90), nullable=True)
    telefono = db.Column(db.String(90), nullable=True)
    correo = db.Column(db.String(90), nullable=True)
    cedula = db.Column(db.String(90), nullable=True)
    imgper = db.Column(db.String(300), nullable=True)
    feccre = db.Column(db.Date(), nullable=True)
    tipousu = db.Column(db.Integer, nullable=True)
    
    def get_id(self):
        return str(self.iduser)
    
    def get_img(self, img_attr):
        return getattr(self, img_attr) if getattr(self, img_attr) else "usuario.png"
    
    def get_img2(self):
        """Retorna la imagen de perfil del usuario o una imagen por defecto."""
        return f"imagenes/{self.imgper}" if self.imgper else "imagenes/casco1.webp"