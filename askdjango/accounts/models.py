# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Profile(models.Model):
#    user = models.ForeignKey('auth.User') BAD CASE
#    user = models.OneToOneField(User) # BAD CASE
#    user = models.OneToOneField('auth.User') BADCASE
    user = models.OneToOneField(settings.AUTH_USER_MODEL) # GOOD CASE
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)