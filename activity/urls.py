from django.conf.urls import url
from . import views
app_name = 'activity'
urlpatterns = [
	url(r'^$',views.index,name = 'index_url_name'),
	url(r'^create/',views.create_activity,name = 'url_name_create'),
	url(r'^list/',views.list,name='list'),
	url(r'^remove/',views.list,name='remove'),
	url(r'^detail/(?P<pkd>[0-9]+)/',views.detail,name='detail')
]