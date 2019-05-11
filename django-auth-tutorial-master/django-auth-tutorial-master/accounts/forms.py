from django import forms
from django.forms import ModelForm
from .models import fileupload

class fileform(forms.ModelForm):
	class Meta:
		model=fileupload
		fields=('url',)