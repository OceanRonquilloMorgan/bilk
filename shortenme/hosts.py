from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'bilk.herokuapp.com', settings.ROOT_URLCONF, name='www'),
)
