from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
<<<<<<< HEAD
from .models import Client
admin.site.register(Client)
=======
from .models import CustomUser
admin.site.register(CustomUser)
<<<<<<< HEAD
=======
>>>>>>> dd989e37e6605b8cf9d8c285b57c947dab1c5718
>>>>>>> 5a10d5e265417f4264e06c140637426d53e0ba80
>>>>>>> 020a4c814ae2449d0d76c08409f853a7e2eb467c
