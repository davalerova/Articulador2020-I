from django import forms
from django.db import *

from .models import *
from django.contrib.auth.models import User



class MiembroForm( forms.ModelForm ):

    class Meta:
        model = Miembro
        fields = ['username', 'first_name', 'last_name',
                  'email', 'sede', 'rol_miembro']
        labels = {'username': 'Correo institucional'}
        widget = {'username': forms.EmailInput,
                  }

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )