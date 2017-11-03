from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
app_name = 'account'
urlpatterns =[
	url(r'^$',views.login,name='login'),

	# login / logout urls
	
]