from django.conf.urls import url
from apps.producto.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^establecimiento$', establecimiento , name='establecimiento'),
    url(r'^publicar$', publicar , name='publicar'),


]
