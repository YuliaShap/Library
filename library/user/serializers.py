from rest_framework import serializers
from authentication.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email', 'password', 'created_at', 'updated_at',
                  'role', 'is_active', 'is_staff', 'is_superuser']

