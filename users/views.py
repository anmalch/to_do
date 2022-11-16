from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serialiazers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
