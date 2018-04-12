from .models import *
from django import forms

class TemplateForm(forms.ModelForm):
	titulo=forms.CharField(widget=forms.TextInput (attrs={ 'size': '52'}))
	fondo =  forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept':'image/*','type': 'file', 'id': 'fondo'}))
	imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept':'image/*','type': 'file', 'id': 'imagen'}))
	fondomovil =  forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept':'image/*','type': 'file', 'id': 'fondomovil'}))

	class Meta:
		model = PrincipalPage
		fields = ('titulo', 'fondo', 'fondomovil', 'imagen')

class VistaForm(forms.ModelForm):
	titulo=forms.CharField(widget=forms.TextInput (attrs={ 'size': '52'}))
	imagen =  forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept':'image/*','type': 'file', 'id': 'fondo'}))

	class Meta:
		model = imagenVista
		fields = ('titulo', 'imagen', 'activo')


class ContenidoForm(forms.ModelForm):
	titulo=forms.CharField(widget=forms.TextInput (attrs={ 'size': '52'}))
	imagen =  forms.ImageField(widget=forms.ClearableFileInput(attrs={'accept':'image/*','type': 'file', 'id': 'fondo'}))
	descripcion=forms.CharField(widget=forms.Textarea ())
	descripcioncorta=forms.CharField(widget=forms.Textarea ())
	class Meta:
		model = detalleImagen
		fields = ('titulo', 'imagen', 'descripcion','descripcioncorta','tipo')
