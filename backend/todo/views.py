from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer


class CreateTodoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        todo.is_valid(raise_exception=True)
        todo.save(created_by=request.user)

        return Response(data=TodoSerializer(todo.instance).data, status=status.HTTP_201_CREATED)


class CompleteTodoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        todo = Todo.objects.complete(id, request.user)

        return Response(data=TodoSerializer(todo).data, status=status.HTTP_200_OK)


class ListTodoView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.get_by_user(user)
