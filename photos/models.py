from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

class Photo(models.Model):
	title = models.CharField(max_length=200)
	caption = models.CharField(default= "", max_length=500)
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	image = models.ImageField(null=False, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp"]
