from django.shortcuts import render
from django. http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import Organizer
from .forms import OrganizerModelForm
# Create your views here.
def index(request):
	return HttpResponse("HI This is Organizer App");
def save(request):
	if request.method == 'POST':
		create_form = OrganizerModelForm(request.POST)
		if create_form.is_valid():
			create_form.save()
			messages.add_message(request, messages.SUCCESS, 'Hello world.')
			return HttpResponseRedirect('../')
		else:
			return render(request,'organizer/save.html',{'organizer_form':create_form})
	create_form = OrganizerModelForm()
	return render(request,'organizer/save.html',{'organizer_form':create_form})