from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .factories import TodoFactory
from users.tests.factories import UserFactory
from todo.models import Todo
from todo.serializers import TodoSerializer

CREATE_TODO_URL = reverse('todo:create')
LIST_TODO_URL = reverse('todo:list')


class TodoApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(self.user)

    def test_create_todo_successful(self):
        payload = {
            'description': 'important todo 1'
        }
        response = self.client.post(CREATE_TODO_URL, payload)
        todo = Todo.objects.first()

        self.assertEqual(todo.description, payload['description'])
        self.assertEqual(todo.created_by, self.user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_todo_anonymous_user(self):
        self.client.logout()
        payload = {
            'description': 'important todo 1'
        }
        response = self.client.post(CREATE_TODO_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_complete_todo(self):
        todo = TodoFactory()

        response = self.client.post(
            reverse('todo:complete', args=[todo.id]), {})

        todo = Todo.objects.get(id=todo.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo.status, True)
        self.assertNotEqual(todo.completed_at, None)

    def test_complete_another_user_todo(self):
        another_user = UserFactory(username='another-user')
        todo = TodoFactory(description='todo', created_by=another_user)

        response = self.client.post(
            reverse('todo:complete', args=[todo.id]), {})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_todo_list_for_current_user(self):
        todo1 = TodoFactory(description='todo1')
        todo2 = TodoFactory(description='todo2')

        response = self.client.get(LIST_TODO_URL)
        serializer = TodoSerializer([todo1, todo2], many=True)

        self.assertEqual(response.data, serializer.data)

    def test_user_can_get_another_user_todo(self):
        todo1 = TodoFactory(description='todo1')
        todo2 = TodoFactory(description='todo2')

        another_user = UserFactory(username='another-user')
        todo3 = TodoFactory(description='todo3', created_by=another_user)

        response = self.client.get(LIST_TODO_URL)
        serializer = TodoSerializer([todo1, todo2], many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertNotIn(TodoSerializer(todo3).data, serializer.data)
