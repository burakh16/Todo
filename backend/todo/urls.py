from django.urls import path

from .views import CreateTodoView, CompleteTodoView, ListTodoView

app_name = 'todo'

urlpatterns = [
    path('create/', CreateTodoView.as_view(), name='create'),
    path('complete/<id>/', CompleteTodoView.as_view(), name='complete'),
    path('', ListTodoView.as_view(), name='list'),
]
