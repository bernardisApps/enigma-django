from django.shortcuts import render, redirect
from .models import Carrito

# Create your views here.

def carrito_view(request):
    if request.user.is_authenticated:
        carrito = Carrito.objects.get(usuario=request.user)
        items = carrito.items.all()
        total = carrito.get_total()
        context = {
            'title':'Carrito',
            'items':items,
            'total':total,
        }
        return render(request,'carrito.html', context)
    else:
        return redirect('inicio')
    
def restar_cantidad(request):
    print(request.items)

def sumar_cantidad(request):
    pass

def eliminar_todo(request):
    pass