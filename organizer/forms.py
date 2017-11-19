from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError

from .models import Organizer


class OrganizerModelForm(ModelForm):

	confirm_password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = Organizer
		fields = ['UserName','FirstName','LastName','email', 'password'
		]
		widgets = {'password': forms.PasswordInput(),}
	
	def clean(self):
		cleaned_data = super(OrganizerModelForm,self).clean()
	
		confirm_password = cleaned_data['confirm_password']

		try:
		
			Organizer.objects.get(UserName = cleaned_data['UserName'])
		
		except Organizer.DoesNotExist:
			pass
		else:
			self.add_error('UserName', cleaned_data['UserName']+"      is already exists")
			# raise ValidationError(cleaned_data['UserName']+'already exists for this problem')
		
		if cleaned_data['password'] != confirm_password:
			self.add_error('password', "Password don't match")
			raise forms.ValidationError('Password don match.')

		return cleaned_data

class OrganizerModifyForm(forms.Form):

	UserName = forms.CharField(max_length = 200)
	password = forms.CharField(max_length = 200, widget=forms.PasswordInput())
	confirm_password = forms.CharField(max_length = 200, widget=forms.PasswordInput())
	FirstName = forms.CharField(max_length = 200)
	LastName = forms.CharField(max_length = 200)
	email = forms.EmailField()
	organizer_id = forms.CharField(widget=forms.HiddenInput())
	

	def clean(self):

		cleaned_data = super(OrganizerModifyForm, self).clean()

		id = cleaned_data['organizer_id']

		if id != cleaned_data['UserName']:
			try:
				Organizer.objects.get(UserName=cleaned_data['UserName'])
			except Organizer.DoesNotExist:
				pass
			else:
					self.add_error('UserName', cleaned_data['UserName']+"          is already exists")



		if cleaned_data['password'] != cleaned_data['confirm_password']:
			self.add_error('password', "Password don't match")
			raise forms.ValidationError('Password don match.')

		return cleaned_data		