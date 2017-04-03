from django.contrib import admin
from apps.producto.models import Producto, Establecimiento
# Register your models here.
admin.site.register(Producto)
admin.site.register(Establecimiento)
