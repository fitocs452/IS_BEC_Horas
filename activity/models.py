from django.db import models
import datetime
from organizer.models import Organizer
from student.models import Student
import fernet_fields as ff
# Create your models here.
class Activity(models.Model):
	organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
	students = models.ManyToManyField(Student,through = 'Confirm_state')
	name = ff.EncryptedCharField(max_length = 200)
	description = models.CharField(max_length =200)
	major = ff.EncryptedCharField(max_length = 200)
	start_date = models.DateTimeField('Date',default=datetime.datetime.now)
	time_worth = ff.EncryptedIntegerField(default = 1)
	place = models.CharField(max_length=200)
	number_of_volunteers = models.IntegerField(default = 1)

class Confirm_state(models.Model):
    student = models.ForeignKey(Student)
    activity = models.ForeignKey(Activity)
    assign = models.CharField(max_length=100,default = 'not_confirm')
    class Meta:
	    unique_together = ('student', 'activity',)
    def __str__(self):
    	return self.assign+self.activity.name+self.student.ID
    def __unicode__(self):
        return "%s is checked in %s activity(as %s)" % (self.student, self.activity, self.type)