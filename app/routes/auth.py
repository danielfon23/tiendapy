from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.users import Users
from app.models.productos import Productos
from app.models.categorias import Categorias
from app import db
bp = Blueprint('auth', __name__)

@bp.route('/index')
def index():
    data = Users.query.all()   
    return render_template('index.html', data=data)

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nameuser = request.form['nameuser']
        passworduser = request.form['passworduser']
        
        user = Users.query.filter_by(nameuser=nameuser, passworduser=passworduser).first()

        if user:
            login_user(user)
            flash("logeado satisfactoriamente", "success")
            return redirect(url_for('auth.dashboard'))
        
        flash('Invalida el usuario o contraseña . Por favor intente nuevamente.', 'danger')
    
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    return render_template("login.html")

@bp.route('/dashboard')
@login_required
def dashboard(): 
    users = Users.query.all() 
    dataprod = Productos.query.all() 
    datacategorias = Categorias.query.all()
    print(datacategorias) 
    return render_template("/index.html",datausu=current_user,datausers=users,dataprod=dataprod,datacategorias=datacategorias)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Ha cerrado sesion satisfactoriamente.', 'info')
    return redirect(url_for('auth.login'))

@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nameuser = request.form['nameuser']
        clave = request.form['claveuser']
        new_user =  Users( passworduser=clave,nameuser= nameuser)
        db.session.add(  new_user)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    
    return render_template('/add.html')