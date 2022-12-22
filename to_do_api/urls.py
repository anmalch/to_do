"""to_do_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from webbrowser import get

from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view


from todo.views import TodoModelViewSet, ProjectModelViewSet
from users.views import UserModelViewSet, UserListAPIView
from rest_framework.authtoken import views

schema_view = get_schema_view(
    openapi.Info(
        title='ToDo',
        default_version='v1',
        description='Test API',
        contact=openapi.Contact(email='admin@mail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(AllowAny,),

)

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/<str:version>/users/', UserListAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

]
