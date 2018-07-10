from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import ShortenMeURL

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortener/home.html", {})

# render a page
class HomeView(View):
	# render the django form
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()

		context = {
			"title": "Jivy.",
			"form": the_form
		}

		return render(request, "shortener/home.html", context)

	# process the form
	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)

		context = {
			"title": "Jivy.",
			"form": form
		}

		template = "shortener/home.html"

		# check if url is valid
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = ShortenMeURL.objects.get_or_create(url=new_url)

			context = {
				"object": obj,
				"created": created,
			}

			# if link is valid and successfully created
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		# show approriate screen depending on success
		return render(request, template, context)

# class-based view
class URLRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(ShortenMeURL, shortcode=shortcode)
		# save item
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)