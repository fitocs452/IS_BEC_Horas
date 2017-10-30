from django.shortcuts import render
from student.models import Student
from organizer.models import Organizer
from .forms import LoginForm

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
				login(request, user)
				return HttpResponse('Authenticated'\
										'successfully')
			else:
				user = Organizer.objects.filter(UserName=username, password=password)

				if user.count() > 0:
					login(request, user)
					return HttpResponse('Authenticated'\
											'successfully')
				else:
					return HttpResponse('Disabled account')

		else:
			return HttpResponse('Invalid login')
	else:
		form = LoginForm()
		return render(request, 'account/login.html', {'form': form})				
