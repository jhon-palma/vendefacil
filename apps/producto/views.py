from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Producto, Establecimiento
# Create your views here.
def index(request):
	productos = Producto.objects.filter(activo=1)
	establecimientos = Establecimiento.objects.all()
	establecimientos = Establecimiento.objects.filter(clasificacion = '2')
	establecimientoss = Establecimiento.objects.filter(clasificacion = '1')
	detalle = False
	return render_to_response('index.html',{'productos':productos, 'establecimientos':establecimientos,'establecimientoss':establecimientoss, 'detalle': detalle})


def establecimiento(request):
	if 'establecimiento' in request.GET.keys():
		sitio = Establecimiento.objects.get(id = request.GET['establecimiento'])
		establecimientos = Establecimiento.objects.filter(clasificacion = '2')
		establecimientoss = Establecimiento.objects.filter(clasificacion = '1')
		detalle = True
	return render_to_response('index.html',{'detalle':detalle,'establecimiento':sitio,'establecimientos':establecimientos,'establecimientoss':establecimientoss})

def publicar(request):
	return render_to_response('publica.html')
