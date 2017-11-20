from django.db import models

# Create your models here.
Major_Choices = (
	('Math', 'Math'),
	('Computer Science', 'Computer Science'),
	('Biology', 'Biology'),
	('Physics', 'Physics'),
	('Programming','Programming')
)
class Student(models.Model):
	ID = models.CharField(max_length = 200,unique=True)
	password = models.CharField(max_length = 200)
	Name = models.CharField(max_length = 200)
	LastName = models.CharField(max_length = 200)
	email = models.EmailField()
	major = models.CharField(
		max_length=20,
		choices=Major_Choices,
		default='Math',
	)
	cuota = models.IntegerField(default=50)
