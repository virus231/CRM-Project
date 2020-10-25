from django.db import models

# Create your models here.
client_status = (
                ('1', 'New Client'),
                ('2','Client In Progress'),
                ('3', 'Client Processed'),
                )

class Client(models.Model):
    mobile = models.CharField(max_length = 13, default = 'Mobile', unique=True)
    status = models.CharField(max_length=9, choices=client_status, default='1')