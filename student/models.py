from django.db import models

# Create your models here.
class Student(models.Model):
	ID = models.CharField(max_length = 200,unique=True)
	password = models.CharField(max_length = 200)
	Name = models.CharField(max_length = 200)
	LastName = models.CharField(max_length = 200)
	email = models.EmailField()
	major = models.CharField(max_length = 200)
	cuota = models.IntegerField(default=50)
