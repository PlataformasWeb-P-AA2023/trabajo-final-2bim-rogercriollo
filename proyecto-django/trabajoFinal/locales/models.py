from django.db import models

class Barrios(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField(max_length=10)
class Personas(models.Model):
    nombres = models.CharField(max_length=300)
    apellidos = models.CharField(max_length=300)
    cedula = models.CharField(max_length=10)
    correo = models.EmailField()

class Localcomida(models.Model):
    propietario = models.ForeignKey(Personas, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=300)
    barrio = models.ForeignKey(Barrios, on_delete=models.CASCADE)
    comida_tipo = models.CharField(max_length=500, )
    ventas_proyectadas = models.FloatField()
    permiso_pago = models.FloatField()

    def save(self):
        self.permiso_pago =self.ventas_proyectadas * 0.8
        return super(Localcomida, self).save()

class Localrepuestos(models.Model):
    propietario = models.ForeignKey(Personas, on_delete=models.CASCADE)
    direccion = models.CharField(verbose_name = "direccion", max_length=300)
    barrio = models.ForeignKey(Barrios, on_delete = models.CASCADE)
    valor_mecaderia = models.FloatField()
    comida_tipo = models.CharField(max_length= 50)
    ventas_proyectadas = models.FloatField()
    permiso_pago = models.FloatField()

    def save(self):
        self.permiso_pago =float(self.ventas_proyectadas * float(0.001))
        return super(Localrepuestos, self).save()