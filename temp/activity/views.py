from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

import datetime
from .models import Activity
from .forms import ActivityForm
from organizer.models import Organizer
from student.models import Student
from datetime import timedelta
# Create your views here.
def index(request):
	return HttpResponse('I am in activity app');
def check_out(request):
	username = '1111'
	type = 'student'
	if type != 'student':
		return render(request,'activity/activity_list.html',{'activities':'asdfsadf'})
	if request.method == "POST":
		act_id = request.POST['activity_id']
		act = Activity.objects.get(pk = act_id)
		act.students.remove(Student.objects.get(ID=username))
		messages.add_message(request, messages.SUCCESS, 'You CheckOut Successfully ')
		return HttpResponseRedirect('../list')
def check_out_detail(request,pkd):
	type = 'student'
	if type != 'student':
		return render(request,'activity/activity_list.html',{'activities':'asdfsadf'})
	activity = Activity.objects.get(pk=pkd)
	duration = activity.start_date+timedelta(hours=activity.time_worth)
	return render(request,'activity/check_out_activity_detail.html',{'act':activity,'duration':duration})
def check_out_list(request):
	username = '1111'
	type = 'student'
	if type != 'student':
		return render(request,'activity/activity_list.html',{'activities':'asdfsadf'})
	activities = Activity.objects.filter(students__ID=username)
	results = [];
	result = [];
	cnt = 0
	for act in activities:			
		result.append(act)
		cnt = cnt + 1
		if cnt == 3:
			results.append(result)
			result = []
			cnt = 0;
	if cnt > 0:
		results.append(result)
	return render(request,'activity/check_out_activity_list.html',{'activities':results})
def check_in(request):
	username = '1111'
	type = 'student'
	if type != 'student':
		return render(request,'activity/activity_list.html',{'activities':'asdfsadf'})
	if request.method == "POST":
		act_id = request.POST['activity_id']
		act = Activity.objects.get(pk = act_id)
		act.students.add(Student.objects.get(ID=username))
		messages.add_message(request, messages.SUCCESS, 'You CheckIn Successfully ')
		return HttpResponseRedirect('../list')
def create_activity(request):
	username = 'Alex'
	if request.method == 'POST':
		create_form = ActivityForm(request.POST)
		if create_form.is_valid():
			instance = create_form.save(commit=False)
			instance.organizer = Organizer.objects.get(UserName = username)
			instance.save()
			messages.add_message(request, messages.SUCCESS, 'Hello world.')
			return HttpResponseRedirect('../list')
		else:
			print(create_form.errors)
	else:
		create_form = ActivityForm()
		return render(request,'activity/create.html',{'activity_form':create_form})
def modify_activity(request,pkd):
	username = 'Alex'
	activity = Activity.objects.get(pk=pkd)
	if request.method == 'POST':
		create_form = ActivityForm(request.POST,instance=activity)
		if create_form.is_valid():
			create_form.save()
			messages.add_message(request, messages.SUCCESS, 'Successfully Modified')
			return HttpResponseRedirect('../../list')
		else:
			print(create_form.errors)
	else:		
		create_form = ActivityForm(instance = activity)
		return render(request,'activity/modify_activity.html',{'activity_form':create_form,'pkd':pkd})
def list(request):
	type = 'student'
	cnt = 0;
	results = [];
	username = '1111'
	if type == 'organizer':
		result = [];
		activities = Activity.objects.all();
		for act in activities:			
			result.append(act)
			cnt = cnt + 1
			if cnt == 3:
				results.append(result)
				result = []
				cnt = 0;
		if cnt > 0:
			results.append(result)
		return render(request,'activity/activity_list.html',{'activities':results})
	if type == 'student':
		stu = Student.objects.get(ID = username)
		act1 = Activity.objects.filter(students__ID=stu).distinct()
		act2 = Activity.objects.filter(students = None)
		activities = Activity.objects.none()
		if act1:
			activities = act1
			if act2:
				act3 = activities | act2
		else:
			activities = act2

		result = [];
		for act in activities:			
			result.append(act)
			cnt = cnt + 1
			if cnt == 3:
				results.append(result)
				result = []
				cnt = 0;
		if cnt > 0:
			results.append(result)
		return render(request,'activity/check_in_activity_list.html',{'activities':results})
def detail(request,pkd):
	type = 'student'
	if type == 'organizer':
		activity = Activity.objects.get(pk=pkd)
		duration = activity.start_date+timedelta(hours=activity.time_worth)
		return render(request,'activity/detail_activity.html',{'act':activity,'duration':duration})
	if type == 'student':
		activity = Activity.objects.get(pk=pkd)
		duration = activity.start_date+timedelta(hours=activity.time_worth)
		return render(request,'activity/check_in_activity_detail.html',{'act':activity,'duration':duration})
def remove(request):
	type = 'organizer'
	if type != 'organizer':
		return render(request,'activity/activity_list.html',{'activities':'asdfsadf'})
	if request.method == "POST":
		remove_id = request.POST['remove_id']
		act = Activity.objects.get(pk = remove_id)
		act.delete()
		messages.add_message(request, messages.SUCCESS, 'Successfully Deleted')
		return HttpResponseRedirect('../list')
