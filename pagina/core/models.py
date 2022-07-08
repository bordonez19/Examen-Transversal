from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCateoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)

    def __str__(self)-> str:
        return self.nombreCategoria

class Producto(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self)-> str:
        return self.descripcion+" "+self.nombre

class Promocion(models.Model):
    idPromocion = models.IntegerField(primary_key=True)
    nombrePromocion = models.CharField(max_length=50)

    def __str__(self)-> str:
        return self.nombrePromocion

class Descuentos(models.Model):
    producto =models.CharField(max_length=50,primary_key=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    descuento = models.IntegerField()
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)

    def __str__(self)-> str:
        return self.descripcion+" "+self.producto