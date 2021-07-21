from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from todo.models import Todo
from users.tests.factories import UserFactory


class ModelTest(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_create_todo_successful(self):
        description = 'very important todo'
        todo = Todo.objects.create(created_by=self.user,
                                   description=description)

        self.assertEqual(todo.description, description)
        self.assertEqual(todo.created_by, self.user)

    def test_create_todo_without_user(self):
        with self.assertRaises(IntegrityError):
            Todo.objects.create(description='test')
