from django.db import models

# Create your models here.
class Persona(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=30)
    job = models.CharField(verbose_name='Trabajo', max_length=30)