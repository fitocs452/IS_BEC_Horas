from django.shortcuts import render,redirect
from django. http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

from .models import Organizer

from .forms import OrganizerModelForm, OrganizerModifyForm

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

	
def modify(request):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	username = request.session['UserName']
	typ = request.session['type']
	if typ != 'organizer':
		return redirect('login')
	else:
		info = Organizer.objects.get(UserName = username)
	
		if request.method == 'POST':
			create_form = OrganizerModifyForm(request.POST)
	
			if create_form.is_valid():
				# create_form.save()
				org = Organizer.objects.get(UserName=username)
				org.UserName = request.POST['UserName']
				request.session['UserName'] = org.UserName
				org.FirstName = request.POST['FirstName']
				org.LastName = request.POST['LastName']
				org.email = request.POST['email']
				org.password = request.POST['password']

				org.save()

				messages.add_message(request, messages.SUCCESS, 'Your Oraganizer account has been updated successfully.')
				return redirect('/activity/list')
			else:
				print(create_form.errors)
				print("not valid")
				return render(request,'organizer/modify.html', {'organizer_form':create_form,})
		else:
			create_form = OrganizerModifyForm(initial={'UserName': info.UserName, 'FirstName': info.FirstName, 'LastName': info.LastName, 'email': info.email,
													'password': info.password, 'confirm_password': info.password, 'organizer_id': info.UserName})
			return render(request,'organizer/modify.html', {'organizer_form':create_form,'info':info})