from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response

from .filters import ProjectFilter
from rest_framework.viewsets import ModelViewSet

from todo.models import Project, Todo
from todo.serialiazers import ProjectModelSerializer, TodoModelSerializer

from rest_framework.permissions import BasePermission


class SuperuserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPaginatonViewSet(ModelViewSet):
    projects = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_deleted = True
        todo.save()
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        return Todo.objects.filter(is_deleted=False)


class TodoDjangoFilterViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    filterset_fields = '__all__'


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoLimitOffsetPaginationViewSet(ModelViewSet):
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination

    def get_queryset(self):
        queryset = Todo.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset
