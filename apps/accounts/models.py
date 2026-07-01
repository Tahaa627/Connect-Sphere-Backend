from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model for Sphere Connect.

    We inherit from AbstractUser so we keep Django's built-in
    authentication features while allowing future customization.
    """

    pass