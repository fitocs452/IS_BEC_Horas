from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.db import IntegrityError

import datetime
from .models import Activity,Confirm_state
from .forms import ActivityForm
from organizer.models import Organizer
from student.models import Student
from datetime import timedelta
# Create your views here.
def index(request):
	return HttpResponse('I am in activity app');
def check_out(request):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	username = request.session['UserName']
	if type != 'student':
		return redirect('login')
	if request.method == "POST":
		act_id = request.POST['activity_id']
		act = Activity.objects.get(pk = act_id)
		# act.students.remove(Student.objects.get(ID=username))
		Confirm_state.objects.get(student = Student.objects.get(ID=username),activity = act).delete()
		messages.add_message(request, messages.SUCCESS, 'You CheckOut Successfully ')
		return HttpResponseRedirect('../list')
def check_out_detail(request,pkd):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	username = request.session['UserName']
	if type != 'student':
		return redirect('login')
	activity = Activity.objects.get(pk=pkd)
	duration = activity.start_date+timedelta(hours=activity.time_worth)
	return render(request,'activity/check_out_activity_detail.html',{'act':activity,'duration':duration})
def check_out_list(request):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	username = request.session['UserName']
	if type != 'student':
		return redirect('login')
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
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	username = request.session['UserName']
	if type != 'student':
		return render(request,'activity/activity_list.html',{'activities':'asdfsadf'})
	if request.method == "POST":
		act_id = request.POST['activity_id']
		act = Activity.objects.get(pk = act_id)
		try:
			confirm_object = Confirm_state.objects.create(student = Student.objects.get(ID=username), activity=act, assign="not_confirm")
			confirm_object.save()
		except IntegrityError as e:
			pass
		messages.add_message(request, messages.SUCCESS, 'You CheckIn Successfully ')
		return HttpResponseRedirect('/activity/list')
		# act.students.add(Student.objects.get(ID=username))
def create_activity(request):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	username = request.session['UserName']
	if request.method == 'POST':
		create_form = ActivityForm(request.POST)
		if create_form.is_valid():
			instance = create_form.save(commit=False)
			instance.organizer = Organizer.objects.get(UserName = username)
			instance.save()
			messages.add_message(request, messages.SUCCESS, 'Create Activity Successfully')
			return HttpResponseRedirect('../list')
		else:
			return render(request,'activity/create.html',{'activity_form':create_form})
	else:
		create_form = ActivityForm()
		return render(request,'activity/create.html',{'activity_form':create_form})
def modify_activity(request,pkd):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	username = request.session['UserName']

	activity = Activity.objects.get(pk=pkd)
	if request.method == 'POST':
		create_form = ActivityForm(request.POST,instance=activity)
		if create_form.is_valid():
			create_form.save()
			messages.add_message(request, messages.SUCCESS, 'Successfully Modified')
			return HttpResponseRedirect('../../list')
		else:
			print("====================")
			print(create_form.errors)
			print("not valid")
			return render(request,'activity/modify_activity.html',{'activity_form':create_form,'pkd':pkd})
	else:		
		create_form = ActivityForm(instance = activity)
		return render(request,'activity/modify_activity.html',{'activity_form':create_form,'pkd':pkd})
def completed(request):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	username = request.session['UserName']
	if type == 'student':
		# activities = Activity.objects.filter(students__ID=username)
		student = Student.objects.get(ID = username)
		activities = Confirm_state.objects.filter(student=student,assign='confirm')
		print("****",username)
		result = [];
		results = []
		cnt = 0
		for acti in activities:
			act=acti.activity
			current_time = datetime.datetime.now()
			native = act.start_date.replace(tzinfo=None)
			if native < current_time:
				result.append(act)
				cnt = cnt + 1
				if cnt == 3:
					results.append(result)
					result = []
					cnt = 0;
		if cnt > 0:
			results.append(result)
		return render(request,'activity/complete_list.html',{'activities':results})
def list(request):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	username = request.session['UserName']
	cnt = 0;
	results = [];

	if type == 'organizer':
		organizer = Organizer.objects.get(UserName=username)
		result = [];
		activities = organizer.activity_set.all();
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
		activities = Activity.objects.exclude(students__ID=username)
		print (activities)
		print("****",username)
		result = [];
		for act in activities:
			current_time = datetime.datetime.now()
			native = act.start_date.replace(tzinfo=None)
			if native < current_time:
				continue
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
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	if type == 'organizer':
		activity = Activity.objects.get(pk=pkd)
		duration = activity.start_date+timedelta(hours=activity.time_worth)
		return render(request,'activity/detail_activity.html',{'act':activity,'duration':duration})
	if type == 'student':
		activity = Activity.objects.get(pk=pkd)
		duration = activity.start_date+timedelta(hours=activity.time_worth)
		return render(request,'activity/check_in_activity_detail.html',{'act':activity,'duration':duration})
def complete_detail(request,pkd):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	if type == 'student':
		activity = Activity.objects.get(pk=pkd)
		duration = activity.start_date+timedelta(hours=activity.time_worth)
		return render(request,'activity/complete_detail.html',{'act':activity,'duration':duration})
def remove(request):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	if type != 'organizer':
		return render(request,'activity/activity_list.html',{'activities':'asdfsadf'})
	if request.method == "POST":
		remove_id = request.POST['remove_id']
		act = Activity.objects.get(pk = remove_id)
		act.delete()
		messages.add_message(request, messages.SUCCESS, 'Successfully Deleted')
		return HttpResponseRedirect('../list')
def assign_student(request,pkd):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	if type!= 'organizer':
		return redirect('login')
	activity = Activity.objects.get(pk=pkd)
	check_in_student = Confirm_state.objects.filter(activity=activity,assign='not_confirm')
	assigned_student = Confirm_state.objects.filter(activity=activity,assign='confirm')
	print('------------')
	print(check_in_student)
	print('------------')
	return render(request,'activity/assign_detail.html',{'act':activity,'check_students':check_in_student,'assigned_students':assigned_student})
def confirm(request,st_id,act_id):
	if request.session.get('type', 'none') == 'none':
		return redirect('login')
	type = request.session['type']
	if type!= 'organizer':
		return redirect('login')
	student = Student.objects.get(pk = st_id)
	act = Activity.objects.get(pk = act_id)
	confirm = Confirm_state.objects.get(activity=act,student=student)
	confirm.assign = 'confirm'
	confirm.save()
	messages.add_message(request, messages.SUCCESS, 'Confirm Successfully ')
	return redirect('/activity/assign/'+act_id)


