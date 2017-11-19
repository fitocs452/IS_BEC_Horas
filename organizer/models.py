from django.db import models

# Create your models here.
class Organizer(models.Model):
	UserName = models.CharField(max_length = 200, unique=True)
	FirstName = models.CharField(max_length = 200)
	LastName = models.CharField(max_length = 200)
	email = models.EmailField()
	password = models.CharField(max_length = 200)
	def __str__(self):
		return self.UserName
