from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Carrito_item, Producto
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

def eliminar_item(request, id):
    try:
        Carrito_item.objects.filter(id=id).delete()
        messages.success(request, "Se ha eliminado el producto con éxito.")
        
    except:
        print('error con la base de datos')
    return redirect('carrito')

# views.py

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # Buscar si el item ya existe en el carrito del usuario
    item, creado = Carrito_item.objects.get_or_create(
        usuario=request.user,
        producto=producto,
        defaults={'cantidad': 1}
    )

    if not creado:
        # Ya existía → aumentar cantidad
        item.cantidad += 1
        item.save()

    return redirect('carrito')  # Redirigí a donde quieras

