from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faculty(models.Model):
	user = models.OneToOneField(User)
	faculty_information = HTMLField()
	faculty_title = models.CharField(max_length=10)
	faculty_preview = models.CharField(max_length=200)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name
