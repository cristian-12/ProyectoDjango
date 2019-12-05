from django.db import models

# Create your models here.
# Los modelos son una clase que devuelve un objeto.

# Clase para el modelo etnia.

class Etnia(models.Model):
    NombEtnia = models.CharField(max_length = 50)


    def __unicode__(self):
        return self.NombEtnia

# clase para el modelo tipoDoc

class tipoDoc(models.Model):
    NombTiDo = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombTiDo

# Clase para el modelo  EstaCivil o estado civil.

class EstaCivil(models.Model):
    NombEsCi = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombEsCi

# Clase para el modelo TipoEstu o clasificacion de los estudios
class TipoEstu(models.Model):
    NombTipoEstu = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombTipoEstu

# Clase paa el modelo tipo de logro

class TipoLogr(models.Model):
    NombTiLo = models.CharField(max_length = 50)

    def __str__(self):
        return self.NombTiLo

class Empleos(models.Model):
    Empleos = models.CharField(max_length = 50)

    def __str__(self):
        return self.Empleos