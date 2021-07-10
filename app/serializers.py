
from MusicPro.settings import DATABASES
from .models import *
from rest_framework import serializers




class ProductoSerializer(serializers.ModelSerializer):

    categoria = serializers.CharField(read_only=True, source="categoria.categoria")
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="categoria")
    class Meta:

        model = Producto
        fields = '__all__'
        exceptions = 'categoria'

class Clienteserializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = '__all__'

class Descuentoserializer(serializers.ModelSerializer):

    class Meta:

        model = Descuento
        fields = '__all__'

class Suscripcionserializer(serializers.ModelSerializer):

    class Meta:

        model = Suscripcion
        fields = '__all__'

