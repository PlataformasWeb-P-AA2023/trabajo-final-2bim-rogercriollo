from django.contrib import admin
from .models import Localcomida, Localrepuestos, Barrios, Personas

# Register your models here.

admin.site.register(Barrios)
admin.site.register(Personas)
admin.site.register(Localcomida)
admin.site.register(Localrepuestos)
