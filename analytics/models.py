from django.db import models

# Create your models here.
from shortener.models import ShortenMeURL

class ClickEventManager(models.Manager):
	def create_event(self, shortenMeInstance):
		if isinstance(shortenMeInstance, ShortenMeURL):
			obj, created = self.get_or_create(shortenme_url=shortenMeInstance)
			obj.count += 1
			obj.save()
			return obj.count
		return None

# track analytics of URL
class ClickEvent(models.Model):
	shortenme_url 	= models.OneToOneField(ShortenMeURL)
	count 			= models.IntegerField(default=0)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)
