from django.db import models

# from django.contrib.auth.models import AbstractUser


# Create your models here.
class CommonModel(models.Model):
    # Date
    created_at = models.DateTimeField(
        # when this object first created time
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        # will set this fieled at every updated
        auto_now=True,
    )

    class Meta:
        abstract = True
