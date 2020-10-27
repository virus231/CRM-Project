from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from clients.models import Client

# Create your models here.

class Manager(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    client_id = models.ForeignKey(Client, on_delete = models.CASCADE, null=True)
    is_admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.email