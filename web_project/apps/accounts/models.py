from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class DocInfo(models.Model):
    NombreDrDra = models.CharField(max_length=50, null=False)
    LastName = models.CharField(max_length=50, null=False)
    asignatura = models.CharField(max_length=50, null=False)
    ciclo = models.CharField(max_length=30, null=False)
    carrera = models.CharField(max_length=100, null=False)

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.NombreDrDra, self.LastName)




# Create your models here.
