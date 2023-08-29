from django.db import models

class Barrios(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre}____ {self.siglas}" 


class Personas(models.Model):
    nombres = models.CharField(max_length=300)
    apellidos = models.CharField(max_length=300)
    cedula = models.CharField(max_length=10)
    correo = models.EmailField()
    def __str__(self):
        return f"{self.nombres} ___ {self.cedula}" 
class Localcomida(models.Model):
    propietario = models.ForeignKey(Personas, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=300)
    barrio = models.ForeignKey(Barrios, on_delete=models.CASCADE)
    comida_tipo = models.CharField(max_length=500, )
    ventas_proyectadas = models.FloatField()
    permiso_pago = models.FloatField(blank = True , null = True)

    def save(self):
        self.permiso_pago =self.ventas_proyectadas * 0.8
        return super(Localcomida, self).save()
    def __str__(self):
        return f"{self.propietario} ____ {self.comida_tipo}" 

class Localrepuestos(models.Model):
    propietario = models.ForeignKey(Personas, on_delete=models.CASCADE)
    direccion = models.CharField(verbose_name = "direccion", max_length=300)
    barrio = models.ForeignKey(Barrios, on_delete = models.CASCADE)
    valor_mecaderia = models.FloatField()
    comida_tipo = models.CharField(max_length= 50)
    ventas_proyectadas = models.FloatField()
    permiso_pago = models.FloatField(blank = True , null = True)

    def save(self):
        self.permiso_pago =float(self.ventas_proyectadas * float(0.001))
        return super(Localrepuestos, self).save()
    def __str__(self):
        return f"{self.propietario} __________ {self.direccion}" 