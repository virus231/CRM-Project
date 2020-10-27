from django.urls import path
from .views import CustomUserCreate

app_name = 'clients'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_client"),
]
