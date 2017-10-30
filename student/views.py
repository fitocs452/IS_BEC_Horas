from django.shortcuts import render
from django. http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from .models import Student
from .forms import StudentModelForm
# Create your views here.
def index(request):
	return HttpResponse("HI This is Student App");

def create(request):
	if request.method == 'POST':
		create_form = StudentModelForm(request.POST)
		if create_form.is_valid():
			create_form.save()
			messages.add_message(request, messages.SUCCESS, 'Your account has been created successfully.')
			return HttpResponseRedirect('index')
		else:
			return render(request,'student/create.html',{'student_form':create_form})
	else:
		create_form = StudentModelForm()
		return render(request,'student/create.html',{'student_form':create_form})

# def modify(request):
# 	if request.method == 'POST':
# 		modify_form = StudentModelForm(request.POST)
# 		if modify_form.is_valid:
# 			modify_form.save()
# 			message