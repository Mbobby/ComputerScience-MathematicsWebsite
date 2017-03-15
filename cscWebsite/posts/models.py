from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	post_title = models.CharField(max_length=400)
	post_body = HTMLField()
	created_by = models.ForeignKey(User)
	post_preview = models.CharField(max_length=400)
	is_published = models.BooleanField(default=False)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.post_title

	class Meta:
		ordering = ["-pub_date"]