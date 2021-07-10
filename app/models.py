from django.db import models
from django.db.models.base import Model

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=40)
    def __str__(self):
        return self.categoria

class Producto(models.Model):
    codigo = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(null=True, blank=True)



    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=41)
    paterno = models.CharField(max_length=40)
    rut = models.CharField(max_length=9)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    mail = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    mail = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    rut = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut

class DetalleVenta(models.Model):
    tipo_comprovante = models.CharField(max_length=100)
    serie_comprovante = models.CharField(max_length=7)
    fecha_comprovante = models.DateField(max_length=100)
    iva = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.serie_comprovante
    
class Descuento(models.Model):
    codigo_descuento = models.CharField(max_length=7)
    valor_descuento = models.IntegerField()

    def __str__(self):
        return self.codigo_descuento

class Venta(models.Model):
    descripcion = models.CharField(max_length=100)
    total_venta = models.IntegerField()

    def __str__(self):
        return self.total_venta

class Sucursal(models.Model):
    direccion = models.CharField(max_length=100)
    numero_sucursal = models.IntegerField()

    def __str__(self):
        return self.numero_sucursal

class Comuna(models.Model):
    direccion = models.CharField(max_length=100)
    numero_comuna = models.IntegerField()
    numero_sucursal = models.ForeignKey(Sucursal, on_delete=models.DO_NOTHING)
    
    def __ (self):
        return self.numero_sucursal

class Region(models.Model):
    direccion = models.CharField(max_length=100)
    numero_region = models.IntegerField()
    numero_comuna= models.ForeignKey(Comuna,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.numero_region

class Pedido(models.Model):
    numero_pedido = models.IntegerField()
    fecha_pedido = models.DateField(max_length=100)
    iva = models.IntegerField()

    def __int__(self):
        return self.numero_pedido


class Proveedores(models.Model):
    nombre_proveedor = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    mail = models.CharField(max_length=100)
    numero_pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre_proveedor

class Suscripcion(models.Model):
    fecha_suscripcion = models.DateField
    valor_suscripcion = models.IntegerField()
    suscrito = models.IntegerField()