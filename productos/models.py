from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='static/product_image', default='static/IMAGES/producto.png')
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=0)

    def __str__(self):
        return self.nombre
    