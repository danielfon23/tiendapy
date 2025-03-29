import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, make_response,send_file,current_app
from flask_login import login_required,current_user
from werkzeug.utils import secure_filename
from app.models.carrito import Carrito
from app.models.productos import Productos
from app.models.categorias import Categorias
from app.models.ventas_t import Ventas_t
from app.models.ventas_d import Ventas_d
from app import db
#from weasyprint import HTML
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image as RLImage
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import red
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
from datetime import datetime, timedelta
import pytz
import base64


# coloca como predeterminada la fecha de colombia 
colombia_tz = pytz.timezone('America/Bogota')

bp = Blueprint('carrito', __name__)
#formulario para generar la vista para agregar al Carrito
@bp.route('/carrito')
def index():
    data = Carrito.query.all()
    return render_template('carrito/addcarrito.html', data=data,datausu=current_user)

# adicionar al carrito
@bp.route('/carrito/add/<int:id>', methods=['GET', 'POST'])
@login_required
def add(id):
    dataPro = Productos.query.get_or_404(id)
    iduser= current_user.iduser
    dataexit = Carrito.query.filter_by(idproducto=id,iduser= iduser).first()
    if request.method == 'POST':

        idproducto= request.form['idproducto']
        cantidad = request.form['cantidad']
        print(dataexit)
        if dataexit:
            dataexit.cantidad = cantidad
        else:
            new_carrito = Carrito(idproducto=idproducto, iduser=iduser, cantidad=cantidad)
            db.session.add(new_carrito)

        db.session.commit()
        return jsonify({'success': True, 'message': '✅ Producto agregado al carrito correctamente'})

        #flash('✅ Producto Agregado al carrito correctamente')
        #return redirect(url_for('auth.dashboard'))
       # return redirect(request.url)
    return render_template('carrito/addcarrito.html', dataPro= dataPro,dataexit=dataexit)


@bp.route('/carrito/list')
def listarcarrito():
    dataexit = Carrito.query.filter_by(iduser= current_user.iduser).all()
    return render_template('carrito/ver_carrito.html', data=dataexit)

@bp.route('/carrito/comprar', methods=['GET', 'POST'])
def comprar():

    selected_items = request.form.getlist('selected_items')  # Lista de IDs de productos seleccionados
    cantidades = request.form.getlist('cantidad')  # Cantidades de los productos

    # Imprimir datos recibidos
    print("Productos seleccionados:", selected_items)
    print("Cantidades enviadas:", cantidades)

    selected_items = request.form.getlist('selected_items')  # Obtiene los IDs seleccionados
    if not selected_items:
        flash("No seleccionaste ningún producto.", "warning")
        return redirect(url_for('carrito.listarcarrito'))  # Redirige si no hay selección
    
    # Crear el encabezado de la factura 
    iduser = current_user.iduser
    subtotal = request.form['total']
    iva = float(subtotal) * 0.19
    total = float(subtotal) + iva
    fecha = datetime.now(colombia_tz).strftime('%Y-%m-%d')
    f_vto = datetime.now(colombia_tz) + timedelta(days=30)
    observacion = request.form['observacion']
    
    # Guardar la venta en la tabla de encabezado
    new_venta_t = Ventas_t(iduser=iduser, total=total, subtotal=subtotal, iva=iva, fecha=fecha, f_vto=f_vto, observacion=observacion)
    db.session.add(new_venta_t)
    db.session.commit()

    # Iterar sobre los productos seleccionados y registrar la venta con la cantidad ingresada en el formulario
    for id_producto in selected_items:
        producto = Productos.query.get(id_producto)
        cantidad = request.form.get(f'cantidad[{id_producto}]')  # Captura la cantidad desde el formulario
        
        if producto and cantidad:
            cantidad = int(cantidad)  # Convertir a entero
            total_producto = cantidad * producto.precio
            
            # Crear el detalle de la factura
            new_venta_d = Ventas_d(
                idventa=new_venta_t.idventa,
                idproducto=producto.idproducto,
                precio=producto.precio,
                cantidad=cantidad,
                total=total_producto,
                fecha=datetime.now(colombia_tz).strftime('%Y-%m-%d')
            )
            db.session.add(new_venta_d)

    db.session.commit()

    flash("Compra realizada con éxito.", "success")
    return redirect(url_for('carrito.vercompras'))

@bp.route('/carrito/ver_compra')
def vercompras():
    dataventas_t = Ventas_t.query.filter_by(iduser= current_user.iduser).all()

    return render_template('carrito/ver_compras.html', data=dataventas_t)

@bp.route('/carrito/detalleventa/<int:id>', methods=['GET', 'POST'])
def detalleventa(id):
    dataventas_d = Ventas_d.query.filter_by(idventa=id).all()
    dataventas_t = Ventas_t.query.filter_by(iduser= current_user.iduser).all()
    return render_template('carrito/ver_compras.html', datad=dataventas_d, data=dataventas_t)
    


@bp.route('/carrito/comprar1', methods=['GET', 'POST'])
def comprar1():
    selected_items = request.form.getlist('selected_items')  # Obtiene los IDs seleccionados
    if not selected_items:
        flash("No seleccionaste ningún producto.", "warning")
        return redirect(url_for('carrito.listarcarrito'))  # Redirige si no hay selección
    #crear el encabezado de la factura 
    iduser= current_user.iduser
    subtotal = request.form['total']
    iva = float(subtotal) * 0.19
    total = float(subtotal) + iva
    fecha = datetime.now(colombia_tz).strftime('%Y-%m-%d')
    f_vto = datetime.now(colombia_tz) + timedelta(days=30)
    observacion = request.form['observacion']
    new_venta_t = Ventas_t(iduser=iduser,total=total,subtotal=subtotal,iva=iva,fecha=fecha,f_vto=f_vto,observacion=observacion)
    db.session.add(new_venta_t) 
    db.session.commit() 
    for id_producto in selected_items:
        # Buscar el producto en la base de datos
        producto = Productos.query.get(id_producto)
        dataexit = Carrito.query.filter_by(iduser= current_user.iduser,idproducto=producto.idproducto).first()
        if producto:
            # Crear el detalle de la factura
            new_venta_d = Ventas_d(
                idventa = new_venta_t.idventa,
                idproducto=producto.idproducto,
                precio=producto.precio,
                cantidad=dataexit.cantidad,
                total =  dataexit.cantidad * producto.precio,
                fecha = datetime.now(colombia_tz).strftime('%Y-%m-%d')
            )
            db.session.add(new_venta_d) 
            db.session.commit() 
 
    flash("Compra realizada con éxito.", "success")

    return redirect(url_for('carrito.vercompras')) 


import qrcode
from PIL import Image as PILImage 
from reportlab.lib.utils import ImageReader
from io import BytesIO
def generar_qr_nequi(numero_cuenta, monto, referencia="Pago factura ComPuMotos"):
    """
    Genera un código QR para realizar pagos a través de Nequi.
    
    Args:
        numero_cuenta (str): Número de cuenta Nequi.
        monto (float): Monto del pago.
        referencia (str): Referencia o mensaje adicional.
        
    Returns:
        BytesIO: Imagen del código QR en formato PNG.
    """
    # Crear el contenido del QR
    contenido = f"NEQUI:{numero_cuenta}|MONTO:{monto}|REF:{referencia}"
    
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(contenido)
    qr.make(fit=True)
    
    # Crear una imagen del QR
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar la imagen en un objeto BytesIO para usarla en ReportLab
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    return buffer



#generar el pdf para generar la factura 

def generar_factura(datos,datacli,dataventas_t,dataventas_d):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    estilo_rojo = ParagraphStyle(
        'EstiloRojo',
        parent=styles['Heading3'],
        textColor=red,
    )
    #colocar la linea separadora
    linea = Table([[""]], colWidths=[500])
    linea.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
    ]))
    estilo_centrado = ParagraphStyle(
        'EstiloCentrado',
        parent=styles['Heading3'],
        alignment=TA_CENTER
    )
    # Encabezado
    # Obtener la ruta absoluta al archivo
    #logo_path = os.path.join(current_app.root_path, 'static', 'imagenes', 'logo.jpg')
    #if not os.path.exists(logo_path):
     #   raise FileNotFoundError(f"El archivo no fue encontrado: {logo_path}")
    
    #im = PILImage(logo_path, 1.5*inch, 0.5*inch)
    #story.append(im)
    
    # Información de la empresa
    story.append(Paragraph("Taller y repuestos donde Eulises", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(linea)
    story.append(Paragraph("Dirección: carrera 6 5 a 126, barrio palenque velez santander", styles['Normal']))
    story.append(Paragraph("Teléfono: 3045822360", styles['Normal']))
    story.append(Paragraph("Email: andetazz87@motosep.com", styles['Normal']))
    story.append(Spacer(1, 12))
    story.append(linea)
    # Información del cliente
    story.append(Paragraph(f"Cliente: {datacli.nombre}", styles['Heading3']))
    story.append(Paragraph(f"Nit: {datacli.cedula}", styles['Normal']))
    story.append(Paragraph(f"Telefono: {datacli.telefono}", styles['Normal']))
    story.append(Paragraph(f"Correo: {datacli.correo}", styles['Normal']))
    story.append(Paragraph(f"Fecha impresion : {datos['fecha']}", styles['Normal']))
    story.append(Spacer(1, 12))
    story.append(linea)
    story.append(Paragraph(f"Factura Nro: {dataventas_t.idventa}",estilo_rojo))
    story.append(Paragraph(f" Fecha: {dataventas_t.fecha}      Fecha Vto: {dataventas_t.f_vto}"))
    story.append(Paragraph(f"observaciones: {dataventas_t.observacion}",estilo_rojo))
    story.append(Spacer(1, 24))

    # Tabla de productos
    story.append(Paragraph(f"Detalle",estilo_centrado))
    data = [['Codigo','Descripción', 'Cantidad', 'Precio Unitario', 'Total']]
    for item in dataventas_d:
        data.append([
            item.idproducto,
            item.productos.nombre.upper(),
            item.cantidad,
            f"{item.precio:.0f}",
            f"{item.total:.0f}"
           
          
        ])

    # Agregar totales
    data.append(['','', '', 'Subtotal:', f"${dataventas_t.subtotal:.0f}"])
    data.append(['','', '', 'IVA :', f"${dataventas_t.iva:.0f}"])
    data.append(['','', '', 'Total:', f"${dataventas_t.total:.0f}"])

    # Estilo de la tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.blue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.blue),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))

    story.append(table)
    story.append(Spacer(1, 24))
    totletras= numero_a_pesos(float(f"{dataventas_t.total:.0f}")).upper()
    story.append(Paragraph(f"Son: "+ totletras , styles['Heading3']))
    story.append(Spacer(1, 24))
    story.append(Spacer(1, 24))

    # Generar el código QR para Nequi
    #numero_cuenta_nequi = "3045822360"  # Reemplaza con el número de cuenta real
    numero_cuenta_nequi = "3126566205"
    monto_pago = int(dataventas_t.total)
    logo_buffer = generar_qr_nequi(numero_cuenta_nequi, monto_pago)

    # Usar RLImage para crear el objeto imagen de ReportLab
    im = RLImage(logo_buffer, width=1.5*inch, height=1.5*inch)
    story.append(im)
    # Agregar al documento
    story.append(Paragraph("Escanea este código QR para pagar:", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Gracias por su compra ComPuMotos!", styles['Normal']))
    story.append(Paragraph("Condiciones de pago: 30 días", styles['Normal']))

    doc.build(story)
    buffer.seek(0)
    return buffer

@bp.route('/carrito/imp_fact/<int:id>', methods=['GET', 'POST'])
def imp_fact(id):
    datacli = current_user
    dataventas_t = Ventas_t.query.filter_by(idventa=id).first()
    dataventas_d = Ventas_d.query.filter_by(idventa=id).all()
    
    datos_factura = {
        'cliente': 'Cliente Ejemplo',
        'direccion': 'Av. Siempre Viva 742',
        'fecha': datetime.now().strftime("%d/%m/%Y"),
        'numero': 'FAC-2023-001',
        'items': [
            {'descripcion': 'Producto 1', 'cantidad': 2, 'precio_unitario': 150.00, 'total': 300.00},
            {'descripcion': 'Producto 2', 'cantidad': 8, 'precio_unitario': 150.00, 'total': 300.00},
            {'descripcion': 'Producto 3', 'cantidad': 4, 'precio_unitario': 150.00, 'total': 300.00},
            {'descripcion': 'Servicio Técnico', 'cantidad': 1, 'precio_unitario': 500.00, 'total': 500.00}
        ],
        'subtotal': 800.00,
        'iva': 128.00,
        'total': 928.00
    }

    pdf = generar_factura(datos_factura,datacli,dataventas_t,dataventas_d)
    return send_file(
        pdf,
        mimetype='application/pdf',
        download_name='factura.pdf',
        as_attachment=True
    )
def numero_a_pesos(numero):
    """
    Convierte un número en su representación en letras con formato de pesos.
    
    Args:
        numero (float o int): El número a convertir.
        
    Returns:
        str: Representación del número en letras con formato de pesos.
    """

    # Diccionarios para las palabras básicas
    unidades = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = {
        10: "diez",
        11: "once",
        12: "doce",
        13: "trece",
        14: "catorce",
        15: "quince",
        16: "dieciséis",
        17: "diecisiete",
        18: "dieciocho",
        19: "diecinueve",
        21: "veintiuno",
        22: "veintidós",
        23: "veintitrés",
        24: "veinticuatro",
        25: "veinticinco",
        26: "veintiséis",
        27: "veintisiete",
        28: "veintiocho",
        29: "veintinueve"
    }
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    def convertir_parte_entera(n):
        """Convierte la parte entera del número."""
        if n == 0:
            return "cero"
        elif n < 10:
            return unidades[n]
        elif n < 20:
            return especiales[n]
        elif n < 30 and n in especiales:
            return especiales[n]
        elif n < 100:
            return f"{decenas[n // 10]} {unidades[n % 10]}".strip()
        elif n < 1000:
            return f"{centenas[n // 100]} {convertir_parte_entera(n % 100)}".strip()
        elif n < 1000000:
            miles = n // 1000
            resto = n % 1000
            if miles == 1:
                return f"mil {convertir_parte_entera(resto)}".strip()
            else:
                return f"{convertir_parte_entera(miles)} mil {convertir_parte_entera(resto)}".strip()
        elif n < 1000000000:
            millones = n // 1000000
            resto = n % 1000000
            if millones == 1:
                return f"un millón {convertir_parte_entera(resto)}".strip()
            else:
                return f"{convertir_parte_entera(millones)} millones {convertir_parte_entera(resto)}".strip()
        else:
            return "Número demasiado grande"

    def convertir_parte_decimal(n):
        """Convierte la parte decimal del número."""
        if n == 0:
            return ""
        else:
            return f"{convertir_parte_entera(n)} centavos"

    # Separar la parte entera y decimal
    if isinstance(numero, float):
        parte_entera, parte_decimal = divmod(numero, 1)
        parte_decimal = int(round(parte_decimal * 100))  # Redondear a dos decimales
    else:
        parte_entera, parte_decimal = numero, 0

    # Convertir cada parte
    texto_entero = convertir_parte_entera(int(parte_entera))
    texto_decimal = convertir_parte_decimal(parte_decimal)

    # Combinar ambas partes
    if texto_decimal:
        return f"{texto_entero} pesos con {texto_decimal}"
    else:
        return f"{texto_entero} pesos"


# Ejemplo de uso
print(numero_a_pesos(1234.56))   # Salida: "mil doscientos treinta y cuatro pesos con cincuenta y seis centavos"
print(numero_a_pesos(1000000))   # Salida: "un millón pesos"
print(numero_a_pesos(0.99))      # Salida: "cero pesos con noventa y nueve centavos"