from django.conf import settings
from django.db import models

from django_hosts.resolvers import reverse

# Create your models here.

from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


# model manager
class ShortenMeURLManager(models.Manager):
	def all(self,*args,**kwargs):
		return super(ShortenMeURLManager, self).all(*args,**kwargs).filter(active=True)

	# custom command 'refreshcodes'
	def refresh_shortcodes(self):
		qs = ShortenMeURL.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			q.save()
			new_codes += 1
		return "New codes made: {i}".format(i=new_codes)

class ShortenMeURL(models.Model):
	url 		= models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
	shortcode 	= models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	updated 	= models.DateTimeField(auto_now=True) # everytime the model is saved
	timestamp 	= models.DateTimeField(auto_now_add=True) # when model was created
	active		= models.BooleanField(default=True)

	objects = ShortenMeURLManager()

	# override save method
	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		if not "http" in self.url:
			self.url = "http://" + self.url
		super(ShortenMeURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	# returns shortened URL link to user
	def get_short_url(self):
		url_path = "http://bilk.herokuapp.com" + self.shortcode
		return url_path

'''
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''
