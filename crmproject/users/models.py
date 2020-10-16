from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

client_status = (
				('1', 'New Client'),
				('2','Client In Progress'),
				('3', 'Client Processed'),
				)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
<<<<<<< HEAD
=======
    mobile = models.CharField(max_length = 13, default = 'Mobile')
    progress = models.CharField(max_length=9, choices=client_status, default='1')
    
>>>>>>> dd989e37e6605b8cf9d8c285b57c947dab1c5718
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email