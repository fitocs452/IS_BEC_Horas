from django.forms import ModelForm
from django import forms
from .models import Activity
from django.core.exceptions import ValidationError
class ActivityForm(ModelForm):
	class Meta:
		model = Activity
		fields = ['name','description','major','start_date','time_worth','place','number_of_volunteers',
		]
		widgets ={'major': forms.HiddenInput(),}
