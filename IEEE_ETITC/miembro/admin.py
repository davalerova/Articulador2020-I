from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Miembro, Genero, Eps, Ciudad, Barrio, Tipo_sangre, Sede, Rol_miembro

admin.site.register(Miembro)
admin.site.register(Genero)
admin.site.register(Eps)
admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Tipo_sangre)
admin.site.register(Sede)
admin.site.register(Rol_miembro)

