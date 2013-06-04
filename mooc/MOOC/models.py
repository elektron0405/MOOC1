from django.db import models

# Create your models here.

class Notes(models.Model):
        username = models.CharField(max_length=200)
        videoid = models.CharField(max_length=200)
        startTime = models.IntegerField()
        endTime = models.IntegerField()
        content = models.CharField(max_length=500)
	
	def __unicode__(self):
        	return self.content

class Department(models.Model):
    	deptCode = models.CharField(max_length = 10)
    	deptName = models.CharField(max_length = 200)
	def __unicode__(self):
        	return self.deptName

class Course(models.Model):
    	department = models.ForeignKey(Department)
    	name = models.CharField(max_length = 200)
    	code = models.CharField(max_length = 20)
    	startDate = models.DateField()
    	duration = models.PositiveIntegerField()
    	university = models.CharField(max_length = 200)
    	instructor = models.CharField(max_length = 200)
	def __unicode__(self):
        	return self.name
