import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required,current_user
from werkzeug.utils import secure_filename
from app.models.productos import Productos
from app.models.categorias import Categorias
from app import db
import uuid  # Para generar nombres aleatorios únicos
bp = Blueprint('productos', __name__)

# Configuración para la subida de imágenes
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','jfif','webp','bmp'}
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'imagenes')  # Ruta absoluta

# Verificar que la carpeta existe, si no, crearla
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Verifica si la extensión del archivo es válida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def subir_imagen(img, img_actual=None):
    """Guarda una imagen con un nombre aleatorio y elimina la anterior si existe."""
    if img and allowed_file(img.filename):
        # Generar un nombre único aleatorio con la misma extensión
        ext = img.filename.rsplit('.', 1)[1].lower()
        nuevo_nombre = f"{uuid.uuid4().hex}.{ext}"
        filepath = os.path.join(UPLOAD_FOLDER, nuevo_nombre)

        try:
            # Guardar la nueva imagen
            img.save(filepath)
            print(f"✅ Imagen guardada: {filepath}")

            # Eliminar la imagen anterior si existe y no es la predeterminada
            if img_actual and img_actual != "productos.png":
                path_anterior = os.path.join(UPLOAD_FOLDER, img_actual)
                if os.path.exists(path_anterior):
                    os.remove(path_anterior)
                    print(f"🗑 Imagen anterior eliminada: {path_anterior}")

            return nuevo_nombre  # Devuelve el nuevo nombre del archivo

        except Exception as e:
            flash(f"❌ Error al guardar la imagen: {str(e)}", "error")
            print(f"❌ Error al guardar la imagen: {str(e)}")

    return "productos.png"  # Si hay error o la imagen no es válida, usa la predeterminada

def subir_imagen1(img):
    """Guarda una imagen en la carpeta `static/imagenes/` y devuelve el nombre del archivo guardado."""
    if img and allowed_file(img.filename):
        filename = secure_filename(img.filename)  # Asegura un nombre de archivo seguro
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        try:
            img.save(filepath)  # Guarda la imagen
            print(f"✅ Imagen guardada en {filepath}")
            return filename  # Devuelve el nombre del archivo guardado
        except Exception as e:
            flash(f"❌ Error al guardar la imagen: {str(e)}", "error")
            print(f"❌ Error al guardar la imagen: {str(e)}")
    
    return "usuario.png"  # Si hay error o no es una imagen válida, usa una imagen predeterminada



@bp.route('/productos')
def index():
    data = Productos.query.all()
    datacategorias = Categorias.query.all()
    print(datacategorias)
    return render_template('productos/index.html', data=data,datausu=current_user,datacategorias=datacategorias)
@bp.route('/productos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        precio = request.form['precio'] 
        descripcion = request.form['descripcion']
        idcategoria = request.form['idcategoria']

       
        #img1 = 'productos.png'
        new_Producto =  Productos(nombre=nombre,precio=precio,descripcion=descripcion,idcategoria=idcategoria)
       
        # Subir imagen si está en la solicitud
        img1 = subir_imagen(request.files.get('img1'))
        new_Producto.img1= img1
        img2 = subir_imagen(request.files.get('img2'))
        new_Producto.img2= img2
        img3 = subir_imagen(request.files.get('img3'))
        new_Producto.img3= img3
        img4 = subir_imagen(request.files.get('img4'))
        new_Producto.img4= img4
        db.session.add(new_Producto)
        db.session.commit()
        
        return redirect(url_for('productos.index'))
    catdata= Categorias.query.all()
    return render_template('productos/add.html',catdata=catdata,)

@bp.route('/eproductos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    producto = Productos.query.get_or_404(id)  
    if request.method == 'POST':

        producto.nombre = request.form['nombre']
        producto.precio = request.form['precio'] 
        producto.descripcion = request.form['descripcion']
        producto.idcategoria = request.form['idcategoria']

        # Subir la nueva imagen y eliminar la anterior
        if 'img1' in request.files and request.files['img1'].filename:
            producto.img1 = subir_imagen(request.files['img1'], producto.img1)
        if 'img2' in request.files and request.files['img2'].filename:
            producto.img2 = subir_imagen(request.files['img2'], producto.img2)
        try:
            db.session.commit()
        except:
            print("Error en la base de datos")
        return redirect(url_for('productos.index'))

    categorias= Categorias.query.all() 
    return render_template('productos/edit.html',catdata=categorias, Productodata=producto)
