from django import forms

from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apaterno', 'amaterno', 'correo_electronico', 'rfc', 'curp']




