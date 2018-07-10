from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'bilk.herokuapp.com', settings.ROOT_URLCONF, name='bilk.herokuapp.com'),
    # host(r'(?!www).*', 'shortenme.hostsconf.urls', name='wildcard'),
)
