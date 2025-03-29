from flask import Flask, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.units import inch
from io import BytesIO
import datetime

app = Flask(__name__)

def generar_factura(datos):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    # Encabezado
    logo = "static/logo.png"
    im = Image(logo, 1.5*inch, 0.5*inch)
    story.append(im)
    
    # Información de la empresa
    story.append(Paragraph("Empresa S.A.", styles['Title']))
    story.append(Paragraph("Dirección: Calle Falsa 123, Ciudad", styles['Normal']))
    story.append(Paragraph("Teléfono: 555-1234", styles['Normal']))
    story.append(Paragraph("Email: info@empresa.com", styles['Normal']))
    story.append(Spacer(1, 12))

    # Información del cliente
    story.append(Paragraph(f"Cliente: {datos['cliente']}", styles['Heading3']))
    story.append(Paragraph(f"Dirección: {datos['direccion']}", styles['Normal']))
    story.append(Paragraph(f"Fecha: {datos['fecha']}", styles['Normal']))
    story.append(Paragraph(f"Factura #: {datos['numero']}", styles['Normal']))
    story.append(Spacer(1, 24))

    # Tabla de productos
    data = [['Descripción', 'Cantidad', 'Precio Unitario', 'Total']]
    for item in datos['items']:
        data.append([
            item['descripcion'],
            str(item['cantidad']),
            f"${item['precio_unitario']:.2f}",
            f"${item['total']:.2f}"
        ])

    # Agregar totales
    data.append(['', '', 'Subtotal:', f"${datos['subtotal']:.2f}"])
    data.append(['', '', 'IVA (16%):', f"${datos['iva']:.2f}"])
    data.append(['', '', 'Total:', f"${datos['total']:.2f}"])

    # Estilo de la tabla
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))

    story.append(table)
    story.append(Spacer(1, 24))

    # Notas finales
    story.append(Paragraph("Gracias por su compra!", styles['Normal']))
    story.append(Paragraph("Condiciones de pago: 30 días", styles['Normal']))

    doc.build(story)
    buffer.seek(0)
    return buffer

@app.route('/generar-factura')
def generar_factura_route():
    datos_factura = {
        'cliente': 'Cliente Ejemplo',
        'direccion': 'Av. Siempre Viva 742',
        'fecha': datetime.datetime.now().strftime("%d/%m/%Y"),
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

    pdf = generar_factura(datos_factura)
    return send_file(
        pdf,
        mimetype='application/pdf',
        download_name='factura.pdf',
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)