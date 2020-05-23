from django.db import models
from django.contrib.auth.models import AbstractUser

from bases.models import ClaseModelo
# Create your models here.
class Miembro(AbstractUser, ClaseModelo):
    fecha_nacimiento = models.DateField(null=True)
    celular = models.CharField(max_length=15, null=True)