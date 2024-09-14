from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'

    def get_total(self):
        total = sum(item.get_total() for item in self.items.all())
        return total
    
class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

    def get_total(self):
        return self.producto.precio * self.cantidad


