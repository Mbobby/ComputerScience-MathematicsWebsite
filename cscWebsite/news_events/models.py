from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class News(models.Model):
	news_title = models.CharField(max_length=400)
	news_body = HTMLField()
	news_preview = models.CharField(max_length=400)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.news_title

class Events(models.Model):
	event_title = models.CharField(max_length=400)
	event_body = HTMLField()
	event_date = models.DateTimeField()
	event_preview = models.CharField(max_length=400)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.event_title