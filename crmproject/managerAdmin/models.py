from django.db import models

class Manager(models.Model):
	username = models.CharField(max_length = 64, default = 'Title')
	email = models.CharField(max_length = 64, default = 'Title')
	password = models.CharField(max_length = 64, default = 'Title')
	client_id = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null=True)
	is_able  = models.BooleanField()
	is_admin = models.BooleanField()