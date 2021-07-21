from todo.models import Todo
from users.tests.factories import UserFactory

import factory
from faker import Factory

faker = Factory.create()


class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo
        django_get_or_create = ('description', 'created_by')
    description = faker.sentence()
    created_by = factory.SubFactory(UserFactory)
