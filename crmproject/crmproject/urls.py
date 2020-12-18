"""crmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from managers.views import ClientViewSet, ManagerViewSet, ManagerPermissions
#from managers.schema import Query
from rest_framework import routers, serializers, viewsets
from django.views.decorators.csrf import csrf_exempt
#from graphene_django.views import GraphQLView
from rest_framework_simplejwt import views as jwt_views

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
) 

router = routers.DefaultRouter()
router.register (r'clients', ClientViewSet)
router.register (r'managers', ManagerViewSet)

urlpatterns = [
    # url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('hello/', LoginLogout.as_view(), name='hello'),
    # url(r"users/(?P<pk>[0-9]+)/$", ManagerViewSet.as_view({"get": "retrieve", "post": "create", "put": "update", "delete": "destroy"}), name="user_methods"),

]

urlpatterns += router.urls

