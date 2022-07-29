from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.Elementos.models import ElementoDeportivo, Prestamo, Devolu


class FormularioElementos(forms.ModelForm):
    """Registra un usuario en la base de datos.

        Variables:

            - password1: Contraseña
            - passwor2: Verificacion de la contraseña

    """
    class Meta:
        model = ElementoDeportivo
        fields = ('numero', 'imagen', 'estado', 'sub_categoria', 'disponibilidad')
        widgets = {
            # 'numero': forms.IntegerField(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # ),
            # 'imagen': forms.IntegerField(
            #     attrs={
            #         'class': 'form-control',
            #     }
            # # ),
            # 'estado': forms.Select(
            #
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # ),
            # 'sub_categoria': forms.Select(
            #
            #     attrs={
            #         'class': 'form-control',
            #
            #     }
            # ),
            'disponibilidad': forms.CheckboxInput(

                attrs={
                    'class': 'form-check-input form-check',
                    'type ': 'checkbox',
                    'input': 'checked',

                }
            ),

        }


# class FormularioPrestamo(forms.ModelForm):
#     class Meta:
#         model = Prestamo
#         fields = ('id_estudiante', 'hora_presamto', 'elemento_deportivo')
#         #
#         # widgets = {
#         #     # 'id': forms.TextInput(
#         #     #     attrs={
#         #     #     'class': "form-control mb-3",
#         #     # }),
#         #     'id_estudiante': forms.NumberInput(
#         #         attrs={
#         #             'class': 'form-control',
#         #             'readonly': 'readonly',
#         #
#         #         }
#         #     ),
#         #     # 'fecha_prestamo': forms.DateTimeInput(
#         #     #     attrs={
#         #     #         'class': 'form-control',
#         #     #
#         #     #     }
#         #     # ),
#         #     'hora_presamto': forms.TextInput(
#         #
#         #         attrs={
#         #             'class': 'form-control',
#         #
#         #         }
#         #     ),
#         #     'elemento_deportivo': forms.Select(
#         #
#         #         attrs={
#         #             'class': 'form-control',
#         #
#         #         }
#         #     ),
#         # }


# class FormularioAceptarPrestamo(forms.ModelForm):
#     class Meta:
#         model = Prestamo
#         fields = ('id_estudiante', 'hora_presamto', 'elemento_deportivo', 'estado', 'cancelacion')
#
#         widgets = {
#             'id_estudiante': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             # 'fecha_prestamo': forms.DateTimeInput(
#             #     attrs={
#             #         'class': 'form-control',
#             #
#             #     }
#             # ),
#             'hora_presamto': forms.TextInput(
#
#                 attrs={
#                     'class': 'form-control',
#
#                 }
#             ),
#             'elemento_deportivo': forms.Select(
#
#                 attrs={
#                     'class': 'form-control',
#
#                 }
#             ),
#             'estado': forms.CheckboxInput(
#                 attrs={
#                     # 'checked': True,
#                     'class': 'form-check-input form-check',
#                     'type ': 'checkbox',
#                     'input': 'checked',
#                 }
#             ),
#             'cancelacion': forms.CheckboxInput(
#                 attrs={
#                     'class': 'form-check-input form-check',
#                     'type ': 'checkbox',
#                     'input': 'checked',
#                 }
#             ),
#         }


class FormularioDevolucion(forms.ModelForm):
    class Meta:
        model = Devolu
        fields = ('descripcion', 'estado_entrega')
        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'id': 'descripcion'
                }
            ),
            'estado_entrega': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'estado',
                }
            ),
        }
