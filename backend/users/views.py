from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

User = get_user_model()


class CreateUserView(APIView):

    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user = User.objects.create_user(**user.validated_data)
        return Response(status=status.HTTP_201_CREATED)
