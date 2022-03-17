from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.Serializer):
    """
    Serializer is used to converting the python object
    """
    username = serializers.CharField(required=True, max_length=200)
    # first_name = serializers.CharField(max_length=200)
    # last_name = serializers.CharField(max_length=200)
    # mobile = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=30)

    def create(self, validate_data):
        """
        for creating the user
        :param validate_data: validating the api data
        """
        return User.objects.create_user(**validate_data)
