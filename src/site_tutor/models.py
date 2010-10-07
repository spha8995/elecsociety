from django.db import models

class Unit_Of_Study(models.Model):
	unit_of_study_code = models.CharField(max_length=8)
	

class Tutor(models.Model):
	name = models.CharField(max_length=50)
	unit_of_study_name = models.CharField(max_length=50)
	unit_of_study = models.ForeignKey(Unit_Of_Study)
	unit_of_study_mark = models.CharField(max_length=4)
	university = models.CharField(max_length=50)
	rate = models.CharField(max_length=10)
