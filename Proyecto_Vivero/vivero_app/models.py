from django.db import models

# Create your models here.
class Productor(models.Model):
    Documento = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"
    
class Finca(models.Model):
    NumCatastro = models.IntegerField(primary_key=True)
    Municipio = models.CharField(max_length=100)
    Productor = models.ForeignKey(Productor,on_delete=models.CASCADE,related_name='Fincas')
    
class Vivero(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    TipoDeCultivo = models.CharField(max_length=100)
    Finca = models.ForeignKey(Finca,on_delete=models.CASCADE,related_name='Viveros')
    
class Labor(models.Model):
    #ID = models.IntegerField(max_length=3,primary_key=True)
    Fecha = models.DateTimeField(auto_now=True)
    Descripcion = models.CharField(max_length=100)
    Vivero = models.ForeignKey(Vivero,on_delete=models.CASCADE,related_name='Labores')
    
class ProductoControl(models.Model):
    RegistroICA = models.IntegerField(primary_key=True)
    NombreProducto = models.CharField(max_length=50)
    Frecuencia = models.CharField(max_length=50)
    ValorProducto = models.DecimalField(max_digits=10, decimal_places=2)
    Labor = models.ForeignKey(Labor,on_delete=models.CASCADE,related_name='ProductosControl')
    
class ControlHongo(ProductoControl):
    PeriodoCarencia = models.IntegerField()
    NombreHongo = models.CharField(max_length=100)
    ProductoControl = models.ForeignKey(ProductoControl,on_delete=models.CASCADE,related_name='ControlHongo')

class ControlPlaga(ProductoControl):
    PeriodoCarencia = models.IntegerField()
    ProductoControl = models.ForeignKey(ProductoControl,on_delete=models.CASCADE,related_name='ControlPlaga')

class ControlFertilizante(ProductoControl):
    FechaUltimaAplicacion = models.DateField()
    ProductoControl = models.ForeignKey(ProductoControl,on_delete=models.CASCADE,related_name='ControlFertilizante')
    
    
    
    
