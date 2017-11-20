from django.conf.urls import url
from . import views
app_name = 'activity'
urlpatterns = [
	# url(r'^$',views.index,name = 'index_url_name'),
	url(r'^create/',views.create_activity,name = 'url_name_create'),
	url(r'^list/',views.list,name='list'),
	url(r'^remove/',views.remove,name='remove'),
	url(r'^detail/(?P<pkd>[0-9]+)/',views.detail,name='detail'),
	url(r'^modify/(?P<pkd>[0-9]+)/',views.modify_activity,name='modify'),
	url(r'^detail/(?P<pkd>[0-9]+)/',views.detail,name='check_in_detail'),
	url(r'^check_in/',views.check_in,name='check_in'),
	url(r'^check_out_list/',views.check_out_list,name='check_out_list'),
	url(r'^check_out/(?P<pkd>[0-9]+)/',views.check_out_detail,name='check_out_detail'),
	url(r'^check_out/',views.check_out,name='check_out'),
	url(r'^assign/(?P<pkd>[0-9]+)/',views.assign_student,name = 'assign'),
	url(r'^confirm/(?P<st_id>[0-9]+)/(?P<act_id>[0-9]+)/',views.confirm,name='confirm'),
	url(r'^complete_list/',views.completed,name='complete_list'),
	url(r'^complete_detail/(?P<pkd>[0-9]+)/',views.complete_detail,name='complete_detail'),	
]