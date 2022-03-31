import logging

from rest_framework.exceptions import ValidationError
from user.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import auth

from user.utils import EncodeDecodeToken

logging.basicConfig(filename="views.log", filemode="w")


class UserRegistration(APIView):
    def post(self, request):
        """
        this method is created for inserting the data
        :param request: format of the request
        :return: Response
        """
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.create(validate_data=serializer.data)
            return Response(
                {
                    'message': "Successfully Registered"
                },
                status=status.HTTP_201_CREATED
            )

        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "validation failed"
                },
                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "data storing failed"
                },
                status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    """
    This class is created for login api
    """

    def post(self, request):
        """
        This method is created for user login
        :param request: web request for login the user
        :return:response
        """
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                encoded_token = EncodeDecodeToken.encode_token(user.pk)
                return Response(
                    {
                        "message": "logged in successfully",
                        "data": {"token": encoded_token}
                    }, status=status.HTTP_200_OK)
            return Response(
                {
                    "message": "login failed No user"
                },
                status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            logging.error("Authentication failed")
