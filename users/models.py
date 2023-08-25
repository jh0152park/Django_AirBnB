from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # Name
    name = models.CharField(max_length=128, default="")
    first_name = models.CharField(max_length=128, blank=True, editable=False)
    last_name = models.CharField(max_length=128, blank=True, editable=False)
    # Host or Staff
    is_host = models.BooleanField(default=False)
    pass
