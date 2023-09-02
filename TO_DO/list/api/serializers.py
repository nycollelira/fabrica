from rest_framework import serializers
from list.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['usuário', 'título','descrição','completo','criar']