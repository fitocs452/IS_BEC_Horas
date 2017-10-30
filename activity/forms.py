from django.forms import ModelForm
from .models import Activity
class ActivityForm(ModelForm):
	class Meta:
		model = Activity
		fields = ['name','description','major','start_date','time_worth','place','number_of_volunteers',
		]

