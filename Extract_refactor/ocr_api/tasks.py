# celery_example/tasks.py
from __future__ import absolute_import, unicode_literals


from Extract_refactor.celery import app
from Ocr.LectorTextoEnImagenes import main

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


@app.task
def orc(nombre, proceso):
    return main(nombre, proceso)


@app.task
def prueba_resta(x, y):
    return x - y

@app.task
def enviar_email(asunto, contenido):
    subject = asunto
    message = contenido
    from_email = 'admin.ExtraxtPdf@hotmail.com'
    if subject and message:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Error al enviar mensaje.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Datos no introducidos')
