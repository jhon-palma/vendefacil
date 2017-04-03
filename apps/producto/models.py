from django.db import models

# Create your models here.
class Producto(models.Model):
	titulo = models.CharField(max_length = 30)
	descripcion = models.TextField()
	precio = models.FloatField(null=False)
	responsable = models.CharField(max_length = 40)
	telefono = models.CharField(max_length=10)
	marca = models.CharField(max_length = 20)
	modelo = models.CharField(max_length = 20)
	color = models.CharField(max_length = 20)
	localizacion = models.CharField(max_length = 20)
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	activo = models.IntegerField()
	img1 = models.ImageField( upload_to = 'uploads/')
	img2 = models.ImageField( upload_to = 'uploads/')
	img3 = models.ImageField( upload_to = 'uploads/')
	img4 = models.ImageField( upload_to = 'uploads/')
	img5 = models.ImageField( upload_to = 'uploads/')

	def __str__(self):
		return self.titulo

class Establecimiento(models.Model):
	nombre = models.CharField(max_length = 40)
	descripcion = models.TextField()
	direcccion = models.CharField(max_length=40)
	telefono = models.CharField(max_length=10)
	responsable = models.CharField(max_length = 40)
	cordenadas = models.TextField()
	horario = models.CharField(max_length=40)
	logo = models.ImageField( upload_to = 'uploads/')
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	activo = models.IntegerField()
	clasificacion = models.IntegerField()
	categoria = models.TextField()

	def __str__(self):
		return self.nombre
