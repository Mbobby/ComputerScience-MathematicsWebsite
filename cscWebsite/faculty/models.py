from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Faculty(models.Model):
	user = models.OneToOneField(User)
	faculty_information = models.TextField()

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name
