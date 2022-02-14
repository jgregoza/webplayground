from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, 
    help_text="Requerido, 250 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):      # validacion de campo para email. Comprueba si existe ya.
        email = self.cleaned_data.get("email")      # recuperamos el email
        if User.objects.filter(email=email).exists():     # comprovamos si exite
            raise forms.ValidationError("Email ya registrado")     # si existe convocamos un eror de validacion y enviamos un mesaje
        return email       # si no existe no entra al Raise y entraria al email del princiopio y lo registraria
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio':forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'link':forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }
 
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields = ['email']
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:        # Si el campo email ha cambiado 
            if User.objects.filter(email=email).exists():       # Si email existe
                raise forms.ValidationError("Email ya registrado")
        return email 