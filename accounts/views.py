from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

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