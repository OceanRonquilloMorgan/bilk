import random
import string

from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

#from shortener.models import ShortenMeURL

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # return ''.join(random.choice(chars) for _ in range(size))
    new_code= ''
     for _ in range(len):
         new_code += random.choice(chars)

     new_code = "http://bilk.herokuapp.com/{0}".format(new_code)
     return new_code


def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance, size=size)
    return new_code
