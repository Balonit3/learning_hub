from django.db import models
from django.contrib.auth.models import AbstractUser
from django.views.debug import default_urlconf


# Create your models here.
class CustomUser(AbstractUser):
    is_instructor = models.BooleanField(default=False)
