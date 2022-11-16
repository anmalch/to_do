from rest_framework.serializers import ModelSerializer, StringRelatedField

from todo.models import Project, Todo


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    author = StringRelatedField

    class Meta:
        model = Todo
        fields = '__all__'
