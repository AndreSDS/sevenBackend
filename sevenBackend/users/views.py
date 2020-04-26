from sevenBackend.users.models import User
from django.http import JsonResponse
from sevenBackend.users.serializers import UserSerializer
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer