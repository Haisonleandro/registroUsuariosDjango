from django.db import models

# Create your models here.

#new
class persona(models.Model):
    ESTADO_CHOICES = [
        ('activo','Activo'),
        ('inactivo', 'Inactivo')
    ]
    name = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    estado = models.CharField(max_length=100,
    choices=ESTADO_CHOICES, default='activo')
    dataCreated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name