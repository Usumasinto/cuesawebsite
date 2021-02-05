import os
import shutil

import qrcode
import qrcode.image.svg

import pyqrcode
import base64
import io

from reportlab.graphics.barcode import qr
from reportlab.lib.units import mm
from django.contrib.staticfiles import finders
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import  UserForm, Docs
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import DocInfo
from io import BytesIO
import reportlab
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab_qrcode import QRCodeImage
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
import qrcode
from PIL import Image

from ... import settings


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu usuario se ha creado correctamente!')
            return redirect('login')
        else:
            messages.warning(request, 'Error al crear cuenta. Tu contraseña debe ser de 8 caracteres o más y no debe ser similar a tu nombre de usuario.')
            return redirect('signup')
    else:
        context = {'form': UserForm()}
        return render(request, 'accounts/signup.html', context)


class profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


def document(request):

    if request.method == "POST":
        form = Docs(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        return render(request, 'accounts/newData.html', {})


def pdfedit(request):
    displayName = DocInfo.objects.filter()
    return render(request, 'accounts/pdf.html', {"DocInfo": displayName})




def renderPdf(request):
    displayName = DocInfo.objects.filter()
    sRoot = settings.STATIC_ROOT
    try:
        context = {
        }



        result = request.POST.get('data', None)
        data2 = request.POST.get('data2', None)
        context['data'] = result
        context2 = {}


        docenteEntry = {
            "name": "",
            "lastname": "",
            "clase": "",
            "carrera": "",
            "ciclo": "",
            'data2': data2
        }

        docente = str(result).split(",")
        docente[0] = docente[0].strip()
        docente[1] = docente[1].strip()
        docente[2] = docente[2].strip()
        docente[3] = docente[3].strip()
        docente[4] = docente[4].strip()

        docenteEntry["name"] = docente[0]
        docenteEntry["lastname"] = docente[1]
        docenteEntry["clase"] = docente[2]
        docenteEntry["carrera"] = docente[3]
        docenteEntry["ciclo"] = docente[4]


        template = get_template('accounts/renderPdf.html')
        html = template.render(docenteEntry)

        qr = qrcode.QRCode(version=1, box_size=5, border=5)
        qr.add_data(docenteEntry)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        img.save("qr.png")

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] ='inline: attachment; filename = "Cuesa.pdf"'



        pisaS = pisa.CreatePDF(html, dest=response)





        if pisaS.err:
            return HttpResponse('hay problemas <pre>' + html + '</pre')
        else:

            return response

    except:
        pass
    return render(request, 'accounts/pdf.html', {"DocInfo": displayName})


# Create your views here.
