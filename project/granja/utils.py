from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
import os

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def send_invoice_email(to_email, pdf, filename):
    email = EmailMessage(
        'Factura Granja El Manantial',
        'Adjunato se encuentra tu factura.',
        'juansol.ay@gmail.com',
        [to_email],
    )
    email.attach(filename, pdf, 'application/pdf')
    email.send()