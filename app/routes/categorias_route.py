import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required,current_user
from werkzeug.utils import secure_filename
from app.models.categorias import Categorias
from app import db

bp = Blueprint('categorias', __name__)

@bp.route('/categorias')
def index():
    data = Categorias.query.all()
    return render_template('categorias/index.html', data=data,datausu=current_user)

@bp.route('/carrusel')
def carrusel():
    data = Categorias.query.all()
    return render_template('categorias/carrusel.html', data=data)

@bp.route('/categorias/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':

        nombre = request.form['nombre']
        new_cat = Categorias(nombre=nombre, img1="categoria.png")
        db.session.add(new_cat)
        db.session.commit()
        flash('✅ Categoria creada correctamente')
        return redirect(url_for('categorias.index'))
    
    return render_template('categorias/add.html')

@bp.route('/categorias/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    categoria = Categorias.query.get_or_404(id)

    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        db.session.commit() 
        flash('✅ Categoria Actualizada correctamente')       
        return redirect(url_for('categorias.index'))

    return render_template('categorias/edit.html', datacat=categoria)



@bp.route('/categorias/delete/<int:id>')
def delete(id):
    user = Categorias.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('categorias.index'))


@bp.route('/categorias/filtro/<int:id>')
def productos_por_categoria(id):
    # Lógica para mostrar productos de la categoría con el id proporcionado
    pass



