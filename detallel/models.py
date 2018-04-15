from django.db import models

# Create your models here.


class PrincipalPage(models.Model):
    titulo = models.CharField(max_length=200)
    fondo = models.ImageField(upload_to='imagenes/')
    fondomovil = models.ImageField(upload_to='imagenes/')
    imagen = models.ImageField(upload_to='imagenes/')

    def __unicode__(self):
        return self.titulo

class imagenVista(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes/')
    ESTADO = (
        (u'A', u'Activo'),
        (u'B', u'Normal'),
    )
    activo = models.CharField(max_length=2, choices=ESTADO,default=u'B', )
    link= models.CharField(max_length=700, null=True)


    def __unicode__(self):
        return self.id


class detalleImagen(models.Model):
    imagenVistaDetalle= models.ForeignKey(imagenVista, on_delete=models.CASCADE)
    idPagina = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to='imagenes/')
    titulo = models.CharField(max_length=80)
    descripcioncorta = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=1300)
    ESTADO = (
        (u'A', u'Incio'),
        (u'B', u'Final'),
        (u'C', u'Normal'),
    )
    tipo = models.CharField(max_length=2, choices=ESTADO,default=u'C', )

