from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
def validate_dataImg(value):
	if not value.name.endswith('.jpg'):
		raise ValidationError(u'not supported file')

def validate_dataMp3(value):
	if not value.name.endswith('.mp3'):
		raise ValidationError(u'not supported file')

class Album(models.Model):
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=32)
	singer = models.CharField(max_length=32)
	cover = models.FileField(validators=[validate_dataImg],upload_to='images/')

	def __str__(self):
		return self.name + '-' + self.singer

class Song(models.Model):

	album = models.ForeignKey(Album,on_delete=models.CASCADE)
	title = models.CharField(max_length=32)
	logo = models.FileField(validators=[validate_dataImg],upload_to='images/')
	music = models.FileField(validators=[validate_dataMp3],upload_to='songs/')
	views = models.IntegerField(default=0)

	def __str__(self):
		return str(self.title)

class Like(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	song = models.ForeignKey(Song,on_delete=models.CASCADE)
	is_liked = models.BooleanField(default=0)

	def __str__(self):
		return str(self.user) + "-" + str(self.song) + "-" + str(self.is_liked)

class View(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	song = models.ForeignKey(Song,on_delete=models.CASCADE)
	views = models.IntegerField(default=0)

	def __str__(self):
		return str(self.user) + "-" + str(self.song) + "-" + str(self.views)


		