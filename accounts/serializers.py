from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True, max_length=20)
    email = serializers.CharField(max_length=255)
    is_staff = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)