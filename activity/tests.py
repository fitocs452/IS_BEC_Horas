from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import reverse
from django.test import Client

from .models import *
from .views import check_in
from .forms import *
from organizer.models import Organizer
from account.views import login
from django.core.management import call_command

# Create your tests here.
class ActivityTests(TestCase):

    def setUp(self):
        call_command('loaddata', 'activity/fixtures/data.json', verbosity=0)
        self.client = Client()
        self.client.login(username='DBarrios', password='123456')

    def test_login(self):
        response = self.client.post(
        	reverse('account:login'),
            data = {
                'username': 'DBarrios',
                'password': '123456'
			}
        )

        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, '/activity/list', fetch_redirect_response=False)

    def test_create_activity(self):
        self.client.post(
        	reverse('account:login'),
            data = {
                'username': 'DBarrios',
                'password': '123456'
			}
        )

        organizer = Organizer.objects.get(UserName='DBarrios')
        Major_Choices = (
			('Math', 'Math'),
			('Computer Science', 'Computer Science'),
			('Biology', 'Biology'),
			('Physics', 'Physics'),
			('Programming','Programming')
		)

        response = self.client.post(
        	reverse('activity:url_name_create'),
            data = {
                'organizer': organizer.id,
                'students': [],
                'name': 'actividad de prueba',
                'description': 'probando actividad',
                'major': Major_Choices,
                'start_date': '2017-11-28 07:39:49-06',
                'time_worth': 5,
                'place': 'UVG',
                'number_of_volunteers': 20
			}
        )

        self.assertEqual(response.status_code, 200)

    def test_list_activity(self):
        self.client.post(
        	reverse('account:login'),
            data = {
                'username': 'DBarrios',
                'password': '123456'
			}
        )

        organizer = Organizer.objects.get(UserName='DBarrios')
        Major_Choices = (
			('Math', 'Math'),
			('Computer Science', 'Computer Science'),
			('Biology', 'Biology'),
			('Physics', 'Physics'),
			('Programming','Programming')
		)

        response = self.client.get(
        	reverse('activity:list')
        )

        self.assertEqual(response.status_code, 200)
