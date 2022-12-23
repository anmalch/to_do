import users as users
from rest_framework.serializers import ModelSerializer, StringRelatedField

from todo.models import Project, Todo
from users.serialiazers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
