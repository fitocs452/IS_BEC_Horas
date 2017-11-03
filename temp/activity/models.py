from django.db import models
import datetime
from organizer.models import Organizer
from student.models import Student
# Create your models here.
class Activity(models.Model):
	organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
	students = models.ManyToManyField(Student,through = 'Confirm_state')
	name = models.CharField(max_length = 200)
	description = models.CharField(max_length =200)
	major = models.CharField(max_length=200)
	start_date = models.DateTimeField('Date',default=datetime.datetime.now)
	time_worth = models.IntegerField(default = 1)
	place = models.CharField(max_length=200)
	number_of_volunteers = models.IntegerField(default = 1)

class Confirm_state(models.Model):
    student = models.ForeignKey(Student)
    activity = models.ForeignKey(Activity)
    type = models.CharField(max_length=100,default = 'not_confirm')
    
    def __unicode__(self):
        return "%s is checked in %s activity(as %s)" % (self.student, self.activity, self.type)