from django.db import models

class Servicios (models.Model):
    titulo = models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    imagen = models.ImageField()
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    def __str__(self):
        return self.titulo
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=10)
    profesion = models.CharField(max_length=20)
    edad = models.IntegerField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def _str_(self):
        return self.nombre