from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.Usuarios.models import Usuario


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):
    """Registra un usuario en la base de datos.

        Variables:

            - password1: Contraseña
            - passwor2: Verificacion de la contraseña

    """
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form.control w-100',
            'placeholder': 'Ingrese se contraseña...',
            'id': 'password1',
            'required': 'required'
        }
    ))

    password2 = forms.CharField(label='Contraseña de confirmacion', widget=forms.PasswordInput(
        attrs={
            'class': 'form.control w-100',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required'
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','username','nombres','apellidos','imagen','is_studet','is_staff','password1')
        widgets = {
            'email' : forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electronico'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'id': 'imagen',
                }
            ),
            'is_studet': forms.CheckboxInput(

                attrs={
                    'checked': True,
                    'class': 'form-check-input form-check',
                    'type ': 'checkbox',
                    'input': 'checked',

                }
            ),
            'is_staff': forms.CheckboxInput(

                attrs={
                    'class': 'form-check-input form-check',
                    'type ': 'checkbox',
                    'input': 'checked',

                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario'
                }
            ),


        }


    def clean_password2(self):
        """Validacion de la contraseña

        Metodo que valida que anvas contraseñas ingresadas sean iguales, esto antes de ser encriptada
        y cuarda en la base dedatos, Retornar la contraseña Validad.

        Exceptiones:
        - ValidationError -- cuando ls contraseñas no son iguales muestra un mensaje error
        """

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinsiden!')
        return password2

    def save(self, commit=True):
        """Incrictar la contraseña y guardar

              Metodo que se encarga de ingrictar contrasena y guardar

               """
        user = super().save(commit= False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user