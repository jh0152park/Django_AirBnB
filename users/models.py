from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class GenderOptions(models.TextChoices):
        MAIL = ("male", "Male")
        FEMAIL = ("female", "Female")
        ABIMAL = ("animal", "Animal")
        THINGS = ("things", "Things")

    class LanguageOptions(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")
        CN = ("cn", "Chinese")
        JP = ("jp", "Japanese")

    class CurrencyOptions(models.TextChoices):
        WON = ("won", "Korean Won")
        USD = ("usd", "Dollar")
        EURO = ("euro", "Euro")

    # Name
    name = models.CharField(
        max_length=128,
        default="",
    )
    first_name = models.CharField(
        max_length=128,
        blank=True,
        editable=False,
    )
    last_name = models.CharField(
        max_length=128,
        blank=True,
        editable=False,
    )

    # Host or Staff
    is_host = models.BooleanField(
        default=False,
    )

    # Profile Pciture
    profile_picture = models.ImageField(
        null=True,
        blank=True,
    )

    # Gender
    gender = models.CharField(
        max_length=10,
        choices=GenderOptions.choices,
        null=True,
    )

    # Language
    language = models.CharField(
        max_length=2,
        choices=LanguageOptions.choices,
        null=True,
    )

    # Currency
    currency = models.CharField(
        max_length=5,
        choices=CurrencyOptions.choices,
        null=True,
    )
    pass
