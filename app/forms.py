from django import forms
from django.forms import ValidationError
from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Descuento, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import TamañoMaximoValidator

class ProductoForm(ModelForm):

    nombre : forms.CharField(min_length=5, max_length=50)
    precio : forms.IntegerField(min_value=1000)

    #def clean_nombre(self):
     #  nom = self.cleaned_data["nombre"]
      # aux = Producto.objects.filter(nombre__iexact=nom).exists()
       #if aux:
        #raise ValidationError("Este producto ya existe. ")

       #return nom

    class Meta:
        model = Producto
        fields = ['nombre','precio','stock','descripcion','categoria','fecha','imagen']
        widgets = {
            'fecha' : forms.SelectDateWidget(years=range(2021,2022))
        }

class UsuarioCreationForm(UserCreationForm):

    def clean_email(self):
        ema = self.cleaned_data["email"]
        aux = User.objects.filter(email__iexact=ema).exists()

        if aux:
            raise ValidationError("correo ya existe. ")

        return ema

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class DescuentoForm(ModelForm):

    codigo_descuento = forms.CharField(max_length=7)
    valor_descuento = forms.IntegerField(min_value=1000)

    #def clean_nombre(self):
     #  nom = self.cleaned_data["nombre"]
      # aux = Producto.objects.filter(nombre__iexact=nom).exists()
       #if aux:
        #raise ValidationError("Este producto ya existe. ")

       #return nom

    class Meta:
        model = Descuento
        fields = ['codigo_descuento','valor_descuento']
