from django import forms

class Formulario_contacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    email = forms.CharField(label='E-mail', required=True)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea) # el parametro widget=forms.Textarea se usa para la renderizcion de este campo de formulario