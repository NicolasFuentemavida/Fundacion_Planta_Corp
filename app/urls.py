from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto',ProductoViewset)
router.register('cliente',ClienteViewset)
router.register('descuento',DescuentoViewset)
router.register('suscripcion',SuscripcionViewset)


urlpatterns = [
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path('contacto/', contacto, name="contacto"),
    path('pago/', pago, name="pago"),
    path('login/', login, name="login"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('modificar/', modificar, name="modificar"),
    path('signup/', signup, name="signup"),
    path('api/',include(router.urls)),
    path('donaciones/', donaciones, name="donaciones"),
    path('suscripcion/', suscripcion, name="suscripcion"),
    path('descuentos/', descuentos, name="descuentos"),
]


