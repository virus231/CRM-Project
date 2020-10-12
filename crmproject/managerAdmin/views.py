from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Manager
from user.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import routers, serializers, viewsets
from .serializer import ManagerSerializer, CustomUserSerializer

def get_manager_by_username(request, username):
	try:
		obj = Manager.objects.get(id=username)
		return HttpResponse (obj.title)
	except ObjectDoesNotExist:
		return 	HttpResponse ("ObjectDoesNotExist")


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ManagerViewSet(viewsets.ModelViewSet):
	queryset = Manager.objects.all()
	serializer_class = ManagerSerializer



def users_list(request):
	if request.method == "GET":
		queryset = CustomUser.objects.all()
		serializer =CustomUserSerializer(queryset, many = True)
		return JsonResponse (serializer.data)