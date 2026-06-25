#formulario registro nuevo para el sistema

from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from django import forms # type: ignore
from .models import Record # type: ignore

class SigupForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Correo electronico'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(SigupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede ser demasiado similar a tu otra información personal.</li><li>Tu contraseña debe contener al menos 8 caracteres.</li><li>Tu contraseña no puede ser una contraseña común.</li><li>Tu contraseña no puede ser completamente numérica.</li></ul>'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingrese la misma contraseña que antes, para verificación.</small></span>'


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}), label=""
    )
    last_name = forms.CharField(
        required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}), label=""
    )
    email = forms.CharField(
        required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), label=""
    )
    phone = forms.CharField(
        required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Teléfono", "class": "form-control"}), label=""
    )
    address = forms.CharField(
        required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Dirección", "class": "form-control"}), label=""
    )
    city = forms.CharField(
        required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control"}), label=""
    )
    state = forms.CharField(
        required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Estado", "class": "form-control"}), label=""
    )
    
    class Meta:
        model=Record
        exclude = ("user",)