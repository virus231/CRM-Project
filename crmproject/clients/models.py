from django.db import models
from managers.models import Manager

# Create your models here.
client_status = (
                ('1', 'New Client'),
                ('2','Client In Progress'),
                ('3', 'Client Processed'),
                )

class Client(models.Model):
    first_name = models.CharField(max_length = 36, default = 'First Name')
    last_name = models.CharField(max_length = 36, default = 'Last Name')
    mobile = models.CharField(max_length = 13, default = 'Mobile', unique=True)
    status = models.CharField(max_length=9, choices=client_status, default='1')
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE, null=True)

    def str(self):
        return self.mobile