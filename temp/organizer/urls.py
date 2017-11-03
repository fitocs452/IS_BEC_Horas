from django.conf.urls import url
from . import views
app_name = 'organizer'
urlpatterns =[url(r'^$',views.index,name='index'),
url(r'^create/',views.save,name='save'),
]