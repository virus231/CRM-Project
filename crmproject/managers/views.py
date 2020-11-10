from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Manager
from clients.models import Client
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.decorators import action
from .serializer import ManagerSerializer, ClientSerializer
from rest_framework.permissions import AllowAny
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def get_manager_by_username(request, username):
	try:
		obj = Manager.objects.get(id=username)
		return HttpResponse (obj.title)
	except ObjectDoesNotExist:
		return 	HttpResponse ("ObjectDoesNotExist")


class UserViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer

    def listing(request):
    	user_list = Client.objects.all()
    	paginator = Paginator(user_list, 2)

    def get_queryset(self):
        page = self.request.query_params.get('page', None)
        offset = 2
        if page:
            return self.queryset[int(page)*offset:int(page)*offset + offset]
        return self.queryset
    # @action(detail = False)
    # def last(self, request):
    # 	return self.queryset.objects.last()

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ManagerSerializer

    def get_queryset(self):
    	# if True:
    	# if self.request.clients.is_admin:
    	# 	if self.request.query_params.get('managers', None):
    	# 		return Manager.objects.filter(p = 'managers')
    	# 	return Manager.objects.all()
    	# return	Manager.objects.filter (manager_id = self.request.)

        if self.request.user.is_admin:
            return Manager.objects.all()
        return Manager.objects.filter(id = self.request.user.id)  

    

class LoginLogout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response()

#viewsets має функції на отримання всіх по індексу - def retrieve, ліста  def list, update, create, delete ...
#class CustomViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin)
#теж передається квері і серіалайзер
# viewsets.ReadOnlyModelViewSet - тільки длля читатння


# def get_users_list(request):
# 	if request.method == "GET":
# 		queryset = Client.objects.all()
# 		serializer =ClientSerializer(queryset, many = True)
# 		return JsonResponse (serializer.data)