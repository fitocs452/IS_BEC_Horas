from django.shortcuts import render,redirect
from django. http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentModelForm, StudentModifyForm

from activity.models import Activity,Confirm_state
# Create your views here.
def index(request):
	if request.session['type'] == 'student':
		return HttpResponse("HI This is Student App");
	else:
		return HttpResponseRedirect('account/login')
def create(request):
	if request.method == 'POST':
		create_form = StudentModelForm(request.POST)
		if create_form.is_valid():
			create_form.save()
			messages.add_message(request, messages.SUCCESS, 'Your account has been created successfully.')
			request.session['type'] = 'student'
			request.session['UserName'] = request.POST['ID']
			return redirect('activity:list')
		else:
			return render(request,'student/create.html', {'student_form':create_form})
	else:
		create_form = StudentModelForm()
		return render(request,'student/create.html', {'student_form':create_form})


def modify(request):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	username = request.session['UserName']
	typ = request.session['type']
	if typ != 'student':
		return render(request,'student/create.html', {'student_form':create_form})

	else:
		info = Student.objects.get(ID= username)
		
		if request.method == 'POST':
			
			create_form = StudentModifyForm(request.POST)
		

			if create_form.is_valid():
				# create_form.save()
				stu = Student.objects.get(ID=username)
				stu.ID = request.POST['ID']
				request.session['UserName'] = stu.ID
				
				stu.Name = request.POST['Name']
				stu.LastName = request.POST['LastName']
				stu.email = request.POST['email']
				stu.major = request.POST['major']
				stu.password = request.POST['password']
				stu.cuota = request.POST['cuota']

				stu.save()

				messages.add_message(request, messages.SUCCESS, 'Your account has been updated successfully.')
				return HttpResponseRedirect('/activity/list')
			else:
				print(create_form.errors)
				print("not valid")
				return render(request,'student/modify.html', {'student_form':create_form,})
		else:
			create_form = StudentModifyForm(initial={'ID': info.ID, 'Name': info.Name, 'LastName': info.LastName, 'email': info.email,
													'major': info.major, 'password': info.password, 'student_id': info.ID,'cuota':info.cuota})
			return render(request,'student/modify.html', {'student_form':create_form,'info':info})
			

		