from django.db import models

# Create your models here.
class CategoriaPro(models.Model):
    nombre = models.CharField(max_length=50)
    created =  models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ='categoria'
        verbose_name_plural ='categorias'

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaPro,on_delete=(models.CASCADE))#si se borra una , todas las detras tambien
    imagen = models.ImageField(upload_to="tienda")
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created =  models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ='producto'
        verbose_name_plural ='productos'

    def __str__(self):
        return self.nombre
