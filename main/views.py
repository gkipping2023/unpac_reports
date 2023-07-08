from django.shortcuts import render
from django.http import HttpResponse

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
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
    return render(request,'main/hoteles.html')

def empresa(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
    return render(request,'main/empresa.html')

def entrenamiento(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_text = request.POST['message-text']
    return render(request,'main/entrenamiento.html')

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