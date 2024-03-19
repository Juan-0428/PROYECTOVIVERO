from django.test import TestCase
from .models import Productor, Finca, Vivero, Labor, ProductoControl, ControlHongo, ControlPlaga, ControlFertilizante

class ProductorTestCase(TestCase):
    def test_productor_creacion(self):
        productor = Productor.objects.create(
            Documento=12345,
            Nombre="Juan",
            Apellido="Perez",
            Correo="juan@example.com",
            Telefono="5551234567"
        )
        self.assertEqual(productor.Documento, 12345)
        self.assertEqual(productor.Nombre, "Juan")
        self.assertEqual(productor.Apellido, "Perez")
        self.assertEqual(productor.Telefono, "5551234567")
        self.assertEqual(productor.Correo, "juan@example.com")

class FincaTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            Documento="12345",
            Nombre="Juan",
            Apellido="Perez",
            Telefono="5551234567",
            Correo="juan@example.com"
        )

    def test_finca_creacion(self):
        finca = Finca.objects.create(
            NumCatastro="123",
            Municipio="Ciudad A",
            Productor=self.productor
        )
        self.assertEqual(finca.Municipio, "Ciudad A")
        self.assertEqual(finca.Productor, self.productor)

class ViveroTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            Documento="12345",
            Nombre="Juan",
            Apellido="Perez",
            Telefono="5551234567",
            Correo="juan@example.com"
        )
        self.finca = Finca.objects.create(
            NumCatastro="123",
            Municipio="Ciudad A",
            Productor=self.productor
        )

    def test_vivero_creacion(self):
        vivero = Vivero.objects.create(
            Codigo="1",
            TipoDeCultivo="Cultivo A",
            Finca=self.finca
        )
        self.assertEqual(vivero.Codigo, "1")
        self.assertEqual(vivero.TipoDeCultivo, "Cultivo A")
        self.assertEqual(vivero.Finca, self.finca)
        
class LaborTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            Documento="12345",
            Nombre="Juan",
            Apellido="Perez",
            Telefono="5551234567",
            Correo="juan@example.com"
        )
        self.finca = Finca.objects.create(
            NumCatastro="123",
            Municipio="Ciudad A",
            Productor=self.productor
        )
        self.vivero = Vivero.objects.create(
            Codigo="1",
            TipoDeCultivo="Cultivo A",
            Finca=self.finca
        )

    def test_labor_creacion(self):
        labor = Labor.objects.create(
            Fecha="2023-09-01",
            Descripcion="Siembra de semillas",
            Vivero=self.vivero
        )
        self.assertEqual(labor.Descripcion, "Siembra de semillas")
        self.assertEqual(labor.Vivero, self.vivero)

class ProductoControlTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            Documento="12345",
            Nombre="Juan",
            Apellido="Perez",
            Telefono="5551234567",
            Correo="juan@example.com"
        )
        self.finca = Finca.objects.create(
            NumCatastro="123",
            Municipio="Ciudad A",
            Productor=self.productor
        )
        self.vivero = Vivero.objects.create(
            Codigo="1",
            TipoDeCultivo="Cultivo A",
            Finca=self.finca
        )
        self.labor = Labor.objects.create(
            Fecha="2023-09-01",
            Descripcion="Siembra de semillas",
            Vivero=self.vivero
        )
    def test_ProductoControl_creacion(self):
        productocontrol = ProductoControl.objects.create(
            RegistroICA =12345,
            NombreProducto = "Producto",
            Frecuencia = "1 por segundo",
            ValorProducto = 12000,
            Labor = self.labor
        )
        self.assertEqual(productocontrol.RegistroICA,12345)
        self.assertEqual(productocontrol.NombreProducto,"Producto")
        self.assertEqual(productocontrol.Frecuencia,"1 por segundo")
        self.assertEqual(productocontrol.ValorProducto,12000)
        self.assertEqual(productocontrol.Labor,self.labor)
'''class ControlHongoTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            Documento="12345",
            Nombre="Juan",
            Apellido="Perez",
            Telefono="5551234567",
            Correo="juan@example.com"
        )
        self.finca = Finca.objects.create(
            NumCatastro="123",
            Municipio="Ciudad A",
            Productor=self.productor
        )
        self.vivero = Vivero.objects.create(
            Codigo="1",
            TipoDeCultivo="Cultivo A",
            Finca=self.finca
        )
        self.labor = Labor.objects.create(
            Fecha="2023-09-01",
            Descripcion="Siembra de semillas",
            Vivero=self.vivero
        )
        self.productocontrol = ProductoControl.objects.create(
            RegistroICA =12345,
            NombreProducto = "Producto",
            Frecuencia = "1 por segundo",
            ValorProducto = 12000,
            Labor = self.labor
        )
    def test_ControlHongos(self):
        hongos = ControlHongo.objects.create(
            PeriodoCarencia = "1semana",
            NombreHongo = "no se",
            ProductoControl = self.productocontrol
        )
        self.assertEqual(hongos.PeriodoCarencia,"1semana")
        self.assertEqual(hongos.NombreHongo,"no se")
        self.assertEqual(hongos.ProductoControl, self.productocontrol)'''
 