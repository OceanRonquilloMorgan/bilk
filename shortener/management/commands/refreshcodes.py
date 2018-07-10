# Creating custom command 'refreshcodes' for terminal use
from django.core.management.base import BaseCommand, CommandError

from shortener.models import ShortenMeURL

class Command(BaseCommand):
    help = 'Refreshes all ShortenMeURL shortcodes'

    def add_arguments(self, parser):
       parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
    	return ShortenMeURL.objects.refresh_shortcodes(items=options['items'])