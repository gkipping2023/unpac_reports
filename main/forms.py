from django.forms import ModelForm
from .models import Comites,Reportes
from django import forms
from datetime import date

class ReportesForm(ModelForm):
    date = forms.DateField(label='Fecha',initial=date.today(),widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    comite = forms.Select(attrs={'class':'form-select'})
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    detalle = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control text-danger'}))
    

    class Meta:
        model = Reportes
        fields = ['date','comite','nombre','apellido','correo','detalle'
        ]