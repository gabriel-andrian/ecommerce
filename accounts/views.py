from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer
import ipdb
class AccountView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = User.objects.create_user(**request.data)
        serializer = UserSerializer(user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(
            {'status': 'Deletado com sucesso'},
            status=status.HTTP_204_NO_CONTENT
        )

class LoginView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(
            username=serializer.data['username'],
            email=serializer.data['email'],
            password=request.data['password']
        )
        ipdb.set_trace()
        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]

            return Response(
                {'token': token.key},
                status=status.HTTP_200_OK
            )

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)