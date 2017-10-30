from django.forms import ModelForm
from .models import Student

from django.core.exceptions import ValidationError

class StudentModelForm(ModelForm):

	class Meta:
		model = Student
		fields = ['ID','Name','LastName', 'password', 'email', 'major', 'cuota',
		]
		
	def clean(self):
		cleaned_data = super(StudentModelForm,self).clean()
		try:
			Student.objects.get(ID=cleaned_data['ID'])
		except Student.DoesNotExist:
			pass
		else:
			self.add_error('ID',cleaned_data['ID']+"          is already exists")
		return cleaned_data
