from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre
    

class Orden(models.Model):
    estados = [
        ('esp', 'En espera'),
        ('prc', 'En proceso'),
        ('fin', 'Finalizado')
    ]
    nombre_Orden = models.CharField(max_length=40,null=True)    
    nombre_cliente = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto,on_delete=models.SET_NULL,null=True)
    llevar = models.BooleanField(default=False)
    estado= models.CharField(choices=estados, max_length=10,default='esp')
    fecha = models.DateField(auto_now_add=True)

