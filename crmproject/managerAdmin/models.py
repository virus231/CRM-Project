from django.db import models
from users.models import CustomUser


class Manager(models.Model):
	username = models.CharField(max_length = 64, default = 'Title')
	email = models.CharField(max_length = 64, default = 'Title')
	password = models.CharField(max_length = 64, default = 'Title')
	client_email = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null=True)
	is_admin = models.BooleanField()