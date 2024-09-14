from django.shortcuts import render, redirect
from productos.models import Producto
from .forms import loginForm, RegistrationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages


# Create your views here.

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

def inicio(request):

    if request.method == 'GET':
        productos = Producto.objects.order_by('-id')[:10]
        context = {
        'title' : 'Inicio',
        'productos' : productos
        }
        return render(request,'inicio.html', context=context)
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        form = loginForm()

        if request.method == 'POST':

            form = loginForm(request.POST)
            if form.is_valid():
                user = authenticate(username = request.POST['username'], password = request.POST['password'])
                if user is not None:
                    login(request, user)
                    return redirect('inicio')
                else:
                    messages.info(request, 'No se pudo loguear revise los datos.')
                    return redirect('login')
        context = {
            'title' : 'login',
            'form' : form
        }
        return render(request, 'login.html',context=context)

def register_view(request):

    if request.user.is_authenticated:
         return redirect('inicio')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(request, 'register.html', {'form':form})