from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings
import os.path
from muzy.settings import MEDIA_URL_TEMP

class Album(models.Model):
	artist = models.CharField(max_length=250, blank=True, null=True)
	album_title = models.CharField(max_length=200, blank=True, null=True)
	genre = models.CharField(max_length=100, blank=True, null=True)
	album_logo = models.CharField(max_length=1000, blank=True, null=True)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		if self.pub_date is None:
			return None
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def __str__(self):
		return self.album_title if self is not None else ""

	def __unicode__(self):
		return self.album_title if self is not None else ""

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=200, blank=True, null=True)
	song_title = models.CharField(max_length=200, blank=True, null=True)
	file = models.FileField(default=None, null=True, upload_to=MEDIA_URL_TEMP)

	def save(self, * args, **kwargs):
		if not self.id:
			filetype = self.file.name.rsplit('.', 1)[1]
			self.file.name = ''.join(e for e in self.file.name if e.isalnum()) + "." + filetype
		return super(Song, self).save(*args, **kwargs)
