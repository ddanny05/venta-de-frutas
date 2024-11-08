from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10)]) 
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    def __str__(self):   #el metodo de devolucion se va a ejecutar siempre
            return self.cedula
class Producto (models.Model):
    codigo_de_producto = models.CharField(max_length=5, primary_key=True, validators=[MinLengthValidator(3),MaxLengthValidator(5)])
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
         return self.codigo_de_producto

class Factura(models.Model):
    Numero_de_factura = models.IntegerField(primary_key= True)
    fecha_de_emision = models.DateField(auto_now_add=True)
    Cedula = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    producto = models.ManyToManyField(Producto)




     