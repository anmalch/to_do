import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from .views import UserModelViewSet
from .models import User
from todo.views import ProjectModelViewSet
from todo.models import Todo, Project


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users', {
            'username': 'writer',
            'first_name': 'Jack',
            'last_name': 'London',
            'email': 'london@gmail.com'
        })
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users', {
            'username': 'writer',
            'first_name': 'Jack',
            'last_name': 'London',
            'email': 'london@gmail.com'
        })
        admin = User.objects.create_superuser('admin', 'admin@post.com', 'admin')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create(username='fermer', first_name='David', last_name='Fermer', email='fermer@post.com')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = User.objects.create(username='fermer', first_name='David', last_name='Fermer', email='fermer@post.com')
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/',
                              {'username': 'fermer', 'first_name': 'Till', 'last_name': 'Fermer',
                               'email': 'fermer@post.com'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = User.objects.create(username='fermer', first_name='David', last_name='Fermer', email='fermer@post.com')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@post.com', 'admin')
        client.login(username='admin', password='admin')
        response = client.put(f'/api/users/{user.id}/', {
            'username': 'fermer', 'first_name': 'Till', 'last_name': 'Fermer', 'email': 'fermer@post.com'})
        user = User.objects.get(pk=user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.first_name, 'Till')
        client.logout()


class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)



