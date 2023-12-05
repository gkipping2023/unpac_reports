from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Reportes
from .forms import ReportesForm

# Create your views here.

def home(request):
    return render(request,'main/home.html')

def itinerarios(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
    return render(request,'main/itinerarios.html')

def hoteles(request):
    reportes_form = ReportesForm()
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
        reportes_form = ReportesForm(request.POST)
        if reportes_form.is_valid():
            reportes_form.save()
    return render(request,'main/hoteles.html',{'reportes_form': reportes_form})

def empresa(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']

        #send email
        send_mail(
            'Reporte de Comite de Empresa' + message_name,
            message_text,
            message_email,
            ['george.kipping@hotmail.com'],
        )
        return render(request,'main/empresa.html',{'message_name':message_name})
    else:
        return render(request, 'main/empresa.html')     
        
def entrenamiento(request):
    reportes_form = ReportesForm()
    if request.method == 'POST':
        reportes_form = ReportesForm(request.POST)
        if reportes_form.is_valid():
            reportes_form.save()
    return render(request,'main/entrenamiento.html',{ 'reportes_form': reportes_form})

def seg_op(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
    return render(request,'main/seg_op.html')

def sal_oc(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
    return render(request,'main/sal_oc.html')

