from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'barrios', BarrioSerializerViewSet)
router.register(r'personas', PersonaSerializerViewSet)
router.register(r'locales_repuestos', LocalesRepuestosSerializerViewSet)
router.register(r'locales_comidas', LocalesComidaViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path("locales-drepuestos", ListLocalesRepuestos, name="listar_loc_repuestos"),

    path("edit/LocalesRepuestos/<int:id>", LocalesRepuestos_edit, name="editar-locales-repuestos"),
    path("eliminarRepuestos/<int:id>", eliminar_LocalesRepuestos, name="eliminar_local_repuestos"),

    path("", ListLocalesComida, name="lista-locales-comida"),

    path("editarlocalescomida/<int:id>", LocalesComida_edit, name="editar-locales-comida"),
    path("eliminarlocalescomida/<int:id>", eliminar_LocalesComida, name="eliminar_local_comida"),
path('login/', ingreso, name="login"),
]
