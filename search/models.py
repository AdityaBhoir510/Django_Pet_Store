from django.db import models
from django.urls import reverse

# Create your models here.
def get_absolute_url(self):
    # from django.core.urlresolvers import reverse
    return reverse('Doglist')
