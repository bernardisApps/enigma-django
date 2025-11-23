from django.shortcuts import render, redirect
from .models import Carrito_item
from django.db.models import Sum, F
from django.contrib import messages

# Create your views here.

def carrito_view(request):
    if request.user.is_authenticated:
        carrito = Carrito_item.objects.filter(usuario=request.user)
        #items = carrito.all()
        total = carrito.aggregate(total=Sum(F('producto__precio') * F('cantidad')))['total'] or 0
        context = {
            'title':'Carrito',
            'carrito':carrito,
            'total':total,
        }
        return render(request,'carrito.html', context)
    else:
        return redirect('inicio')
    
def editar_item(request, id):
    if request.method == 'POST':
        if int(request.POST['cantidad']) > 0:
            Carrito_item.objects.filter(id=id).update(cantidad=request.POST['cantidad'])
            messages.success(request, "Se ha editado el producto con éxito.")
        else:
            Carrito_item.objects.filter(id=id).delete()
            messages.success(request, "Se ha eliminado el producto con éxito.")
        return redirect('carrito')
