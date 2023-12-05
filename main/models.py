from django.db import models

# Create your models here.
class Comites(models.Model):
    comite = models.CharField(max_length=150)

    def __str__(self):
        return self.comite
    
class Reportes(models.Model):
    date = models.DateField()
    comite = models.ForeignKey(Comites, on_delete=models.CASCADE,max_length=20)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=250)
    detalle = models.TextField()
    # imagen = models.ImageField(null=True, blank=True,upload_to='images')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comite