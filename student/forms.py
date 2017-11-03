from django.forms import ModelForm
from .models import Student
from django import forms

from django.core.exceptions import ValidationError

class StudentModelForm(ModelForm):

	confirm_password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Student
		fields = ['ID','Name','LastName', 'password', 'email', 'major', 'cuota',
		]
		widgets ={'password': forms.PasswordInput(),}
		

	def clean(self):
		cleaned_data = super(StudentModelForm,self).clean()
		
		confirm_password = cleaned_data['confirm_password']


		try:
			val = int(cleaned_data['ID'])

		except ValueError:
			self.add_error('ID', " Please Enter Number")

		else:
			
			try:
				Student.objects.get(ID=cleaned_data['ID'])
			except Student.DoesNotExist:
				pass
			else:
				self.add_error('ID', cleaned_data['ID']+"          is already exists")

		if cleaned_data['password'] != confirm_password:
			self.add_error('password', "Password don't match")
			raise forms.ValidationError('Password don match.')

		return cleaned_data

	# def clean_password2(self):

	# 	cd = self.cleaned_data
	# 	if cd['password'] != cd['confirm_password']:
	# 		raise forms.ValidationError('Passwords don\'t match.')
	# 	return cd['password2']
class StudentModifyForm(forms.Form):

	# confirm_password = forms.CharField(widget=forms.PasswordInput())
	ID = forms.CharField(max_length = 200)
	password = forms.CharField(max_length = 200, widget=forms.PasswordInput())
	confirm_password = forms.CharField(max_length = 200, widget=forms.PasswordInput())
	Name = forms.CharField(max_length = 200)
	LastName = forms.CharField(max_length = 200)
	email = forms.EmailField()
	major = forms.CharField(max_length = 200)
	student_id = forms.CharField(widget=forms.HiddenInput())
	# form.fields['field_name'].widget = forms.HiddenInput()


	def clean(self):
		
		cleaned_data = super(StudentModifyForm, self).clean()

		id = cleaned_data['student_id']

		if id != cleaned_data['ID']:
			try:
				val = int(cleaned_data['ID'])

			except ValueError:
				self.add_error('ID', " Please Enter Number")
			else:
				try:
					Student.objects.get(ID=cleaned_data['ID'])
				except Student.DoesNotExist:
					pass
				else:
					self.add_error('ID', cleaned_data['ID']+"          is already exists")
		
		
		if cleaned_data['password'] != cleaned_data['confirm_password']:
			self.add_error('password', "Password don't match")
			raise forms.ValidationError('Password don match.')

		return cleaned_data
		
