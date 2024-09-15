from django.db import models
from PIL import Image

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guarda la imagen original primero

        # Abrir la imagen utilizando Pillow
        img = Image.open(self.imagen.path)

        # Redimensionar si es necesario
        if img.height > 200 or img.width > 200:
            output_size = (200, 150)  # Tamaño máximo permitido
            img.thumbnail(output_size)
            img.save(self.imagen.path)  # Sobreescribir la imagen con el nuevo tamaño

    def __str__(self):
        return self.nombre
    