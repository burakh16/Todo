from django.contrib.auth import get_user_model

import factory

from faker import Factory

User = get_user_model()
faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'test'
    password = factory.PostGenerationMethodCall('set_password', '1234')

    is_active = True
