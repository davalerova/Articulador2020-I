from django.db import models
from IEEE_ETITC.bases import ClaseModelo
class Tipo_Actividad(ClaseModelo):
    descripcion = models.CharField(
        max_length=45,
        help_text='que tipo de actividad es',
        unique=True,
        verbose_name='Descripción'
    )

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Tipo_Actividad, self).save()

    class Meta:
        verbose_name = 'Tipo_Actividad'
        verbose_name_plural = 'Tipo_Actividad'


class Actividad_Interna(ClaseModelo):
    tipo_actividad=models.ForeignKey(Tipo_Actividad,on_delete=False)
    nombre=models.CharField( max_length=45,help_text='Digite nombre de la actividad'
    ,unique=True,
    verbose_name='Descripción')
    descripcion=models.CharField( max_length=45,help_text='Digite nombre de la actividad'
    ,verbose_name='Descripción')
    fecha=models.DateTimeField()
    solo_miembros=models.BooleanField()

# Create your models here.