from rest_framework import serializers
from sevenBackend.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "username", "email", "phone", "website"]