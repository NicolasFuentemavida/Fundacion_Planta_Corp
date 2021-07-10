from re import sub
import django
from django.contrib.auth import authenticate, forms
from django.contrib.auth.models import Permission
from django.core import mail
from django.core.checks import messages
from django.core.paginator import Paginator
from django.db.models.fields import files
from app.forms import *
from app.models import Producto
from django.shortcuts import redirect,render
from django.http import Http404
from django.contrib.auth.decorators import permission_required
from rest_framework import viewsets
from .serializers import *
from django.conf import settings
from django.core.mail import send_mail
from app import forms


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = Clienteserializer

class DescuentoViewset(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = Descuentoserializer

class SuscripcionViewset(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = Suscripcionserializer
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def productos(request):
    productosAll = Producto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productosAll,6)
        productosAll = paginator.page(page)
    except:
        raise Http404
    datos = {
        'listasProductos' : productosAll,
        'paginator' : paginator
    }
    return render(request, 'app/productos.html',datos)

def contacto(request):
    return render(request, 'app/contacto.html')

def pago(request):
    return render(request, 'app/pago.html') 

def login(request):
    return render(request, 'app/login.html') 

def modificar(request):
    productosAll = Producto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productosAll,5)
        productosAll = paginator.page(page)
    except:
        raise Http404
    datos = {
        'listasProductos' : productosAll,
        'paginator' : paginator
    }
    return render(request, 'app/modificar.html',datos) 

@permission_required('app.add_producto')
def agregar_producto (request):
    datos = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto Guardado Correctamente"
        datos['form'] = formulario
    return render(request, 'app/agregar_producto.html', datos)            
 
@permission_required('app.change_producto')    
def modificar_producto (request, id):
    productos = Producto.objects.get(id=id)
    datos = {
        'form' : ProductoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto Modificado Correctamente"
            return redirect(to="modificar")
    return render(request, 'app/modificar_producto.html', datos)  

@permission_required('app.delete_producto')
def eliminar_producto (request,id):
    productos = Producto.objects.get(id=id)
    productos.delete()

    return redirect(to="modificar")

def signup(request):
    datos = {
        'form' : UsuarioCreationForm()
    }
    if request.method == 'POST':
        formulario = UsuarioCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="index")
        datos['form'] = formulario

    return render(request, 'registration/signup.html', datos)

def donaciones(request):
    return render(request, 'app/donaciones.html')

def suscripcion(request):
    return render(request, 'app/suscripcion.html')

@permission_required('app.add_descuentos')
def descuentos(request):
    datos = {
        'form' : DescuentoForm()
    }

    if request.method == 'POST':
        formulario = DescuentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Descuento Guardado Correctamente"
        datos['form'] = formulario
    return render(request, 'app/descuentos.html', datos)   
