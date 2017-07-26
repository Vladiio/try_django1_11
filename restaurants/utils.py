import string
import random

from django.utils.text import slugify


DONT_USE = ['create',]

def random_string_generator(
        size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    slug = new_slug if new_slug is not None else slugify(instance.title)
    Class_ = instance.__class__
    is_exist = Class_.objects.filter(slug=slug).exists()
    if is_exist or slug in DONT_USE:
        slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator())
        return unique_slug_generator(instance, slug)
    return slug
