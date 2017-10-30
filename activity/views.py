from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

import datetime
from .models import Activity
from .forms import ActivityForm
from organizer.models import Organizer
from datetime import timedelta
# Create your views here.
def index(request):
	return HttpResponse('I am in activity app');
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
def list(request):
	activities = Activity.objects.all();
	type = 'organizer'
	cnt = 0;
	results = [];
	if type == 'organizer':
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
		return render(request,'activity/activity_list.html',{'activities':results})
	if type == 'student':
		result = [];
		for act in activities:			
			result.append(act)
			cnt = cnt + 1
			if cnt == 3:
				results.append(result)
				result = []
				cnt = 0;
		return render(request,'activity/check_in_activity_detail.html',{'activities':results})
def detail(request,pkd):
	type = 'organizer'
	if type == 'organizer':
		activity = Activity.objects.get(pk=pkd)
		duration = activity.start_date+timedelta(hours=activity.time_worth)
		return render(request,'activity/detail_activity.html',{'act':activity,'duration':duration})
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
