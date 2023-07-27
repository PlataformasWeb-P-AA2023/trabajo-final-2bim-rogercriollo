from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'barrios', BarrioSerializerViewSet)
router.register(r'personas', PersonaSerializerViewSet)
router.register(r'locales_repuestos', LocalesRepuestosSerializerViewSet)
router.register(r'locales_comidas', LocalesComidaViewSet)



]
