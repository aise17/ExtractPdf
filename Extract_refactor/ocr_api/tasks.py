# celery_example/tasks.py
from __future__ import absolute_import, unicode_literals


from Extract_refactor.celery import app
from Ocr.LectorTextoEnImagenes import main

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


@app.task
def orc(nombre, proceso):
    return main(nombre, proceso)

