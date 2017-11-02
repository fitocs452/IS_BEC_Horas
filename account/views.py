from django.shortcuts import render,redirect
from student.models import Student
from organizer.models import Organizer
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid(): 
			cd = form.cleaned_data		
			username = cd['username']
			password = cd['password']
			
			user = Student.objects.filter(ID=username, password=password)
			if user.count() > 0 :
				request.session['UserName'] = username
				request.session['type'] = 'student'
				
				return redirect('/activity/list')
			else:
				user = Organizer.objects.filter(UserName=username, password=password)

				if user.count() > 0:
					request.session['UserName'] = username
					request.session['type'] = 'organizer'
					
					return redirect('/activity/list')
				else:
					form.add_error('username',"")
					return render(request, 'account/login.html', {'form': form})

		else:
			form.add_error('username',"invalid")			
			return render(request, 'account/login.html', {'form': form})
	else:
		form = LoginForm()
		return render(request, 'account/login.html', {'form': form})				

def logout(request):
    try:
        del request.session['UserName']
        del request.session['type']
    except KeyError:
        pass
    return redirect('login')
@login_required
def dashboard(request):
	return render(request, 'account/activity.html', {'section': 'activity'})