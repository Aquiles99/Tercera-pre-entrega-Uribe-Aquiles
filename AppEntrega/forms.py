from django import forms
 
class CursoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email= forms.EmailField()

class Mi_cuentaFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()


class LibrosFormulario(forms.Form):
    titulo= forms.CharField(max_length=30)
    genero= forms.CharField(max_length=30)
    autor= forms.CharField(max_length=30)
    

class SucursalesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    domicilio= forms.CharField(max_length=30)

class ContactoFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()
