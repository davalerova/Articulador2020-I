from django.db import models
from IEEE_ETITC.bases import ClaseModelo


class miembro (ClaseModelo):
    nombre = models.CharField(max_length=45,
                              help_text='Nombre del usuario',
                              unique=False,
                              verbose_name='Nombre')
    apellido = nombre = models.CharField(max_length=45,
                                         help_text='Digite ',
                                         unique=False,
                                         verbose_name='Apellidos')
    correo_electronico_pnstitucional = models.EmailField()
    correo_electronico_personal = models.EmailField()
    Fecha_De_Nacimientot = models.DateTimeField()
    genero = models.ForeignKey(Genero, on_delete=False)
    eps = models.ForeignKey(Eps, on_delete=False)
    barrio = models.ForeignKey(Barrio, on_delete=False)
    tipo_sangre = models.ForeignKey(Tipo_Sangre, on_delete=False)
    sede = models.ForeignKey(Sede, on_delete=False)
    rol_miembro = models.ForeignKey(Rol_Miembro, on_delete=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'


class Eps(ClaseModelo):
    descripcion = models.CharField(
        max_length=45,
        help_text='Eps Usuario',
        unique=True,
        verbose_name='Eps')

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Eps, self).save()

    class Meta:
        verbose_name = 'Eps'
        verbose_name_plural = 'Eps'


class Ciudad(ClaseModelo):
    descripcion = models.CharField(
        max_length=45,
        help_text='Ciudad de residencia',
        unique=True,
        verbose_name='ciudad')

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Ciudad, self).save()

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudad'


class Genero(ClaseModelo):
    descripcion = models.CharField(
        max_length=45,
        help_text='Género con el que se identifica',
        unique=True,
        verbose_name='Género'
    )

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Genero, self).save()

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'


class Barrio(ClaseModelo):
    descripcion = models.CharField(
        max_length=45,
        help_text='Barrio de Residencia',
        unique=True,
        verbose_name='Barrio'
    )
    ciudad = models.ForeignKey(Ciudad, on_delete=False)

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Barrio, self).save()

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrio'


class Tipo_Sangre(ClaseModelo):
    descripcion = models.CharField(
        max_length=45,
        help_text='Tipo de Sangre',
        unique=True,
        verbose_name='RH'
    )

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Tipo_Sangre, self).save()

    class Meta:
        verbose_name = 'Tipo_Sangre'
        verbose_name_plural = 'Tipo_Sangre'


class Sede(ClaseModelo):
    descripcion = models.CharField(
        max_length=45,
        help_text='sede de donde recibe clases',
        unique=True,
        verbose_name='Sede'
    )

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Tipo_Sangre, self).save()

    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sede'


class Rol_Miembro(ClaseModelo):
    descripcion = models.CharField(
        max_length=45,
        help_text='Puesto que ocupa en la Rama',
        unique=True,
        verbose_name='Rol'
    )

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Tipo_Sangre, self).save()

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Rol'


# Create your models here.
