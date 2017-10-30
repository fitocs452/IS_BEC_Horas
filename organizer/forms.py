from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Organizer

class OrganizerModelForm(ModelForm):
	class Meta:
		model = Organizer
		fields = ['UserName','FirstName','LastName','email',
		]
	def clean(self):
		cleaned_data = super(OrganizerModelForm,self).clean()
		try:
			Organizer.objects.get(UserName = cleaned_data['UserName'])
		except Organizer.DoesNotExist:
			pass
		else:
			self.add_error('UserName', cleaned_data['UserName']+"      is already exists")
			# raise ValidationError(cleaned_data['UserName']+'already exists for this problem')
		return cleaned_data