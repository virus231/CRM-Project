from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Manager
from users.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.decorators import action
from .serializer import ManagerSerializer, CustomUserSerializer
from rest_framework.permissions import AllowAny

def get_manager_by_username(request, username):
	try:
		obj = Manager.objects.get(id=username)
		return HttpResponse (obj.title)
	except ObjectDoesNotExist:
		return 	HttpResponse ("ObjectDoesNotExist")


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    # @action(detail = False)
    # def last(self, request):
    # 	return self.queryset.objects.last()

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ManagerSerializer

#viewsets має функції на отримання всіх по індексу - def retrieve, ліста  def list, update, create, delete ...
#class CustomViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin)
#теж передається квері і серіалайзер
# viewsets.ReadOnlyModelViewSet - тільки длля читатння


# def get_users_list(request):
# 	if request.method == "GET":
# 		queryset = CustomUser.objects.all()
# 		serializer =CustomUserSerializer(queryset, many = True)
# 		return JsonResponse (serializer.data)