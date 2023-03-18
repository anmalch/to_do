import graphene
from graphene_django import DjangoObjectType
from users.models import User
from todo.models import Todo, Project


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all_'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all_'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all_'


class Query(graphene.ObjectType):
    all_project = graphene.List(ProjectType)
    all_user = graphene.List(UserType)
    all_todo = graphene.List(TodoType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    todo_by_project_name = graphene.List(TodoType, name=graphene.String(required=True))

    def resolve_all_project(root, info):
        return Project.objects.all()

    def resolve_all_user(root, info):
        return User.objects.all()

    def resolve_all_todo(root, info):
        return Todo.objects.all()

    def resolve_todo_by_project_name(root, info, name):
        todos = Todo.objects.all()
        if name:
            todos = todos.filter(project__name=name)
        return todos

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            return None


class UserMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.Int(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, first_name, id):
        user = User.objects.get(pk=id)
        user.first_name = first_name
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
