from django import forms
from .models import EnModel

class EnForm(forms.ModelForm):
	class Meta:
		model=EnModel
		fields='__all__'
