from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apaterno = models.CharField(max_length=100)
    amaterno = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rfc = models.CharField(max_length=13, unique=True)
    curp = models.CharField(max_length=18, unique=True)
    

    def __str__(self):
        return self.nombre 