import logging

from rest_framework.exceptions import ValidationError
from user.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import auth

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
                })

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
    def post(self, request):
        """
         Description : - This method is writing Login of user
        :param request:
        :return: Response
        """
        try:
            data = request.data
            username = data.get("username")
            password = data.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                return Response(
                    {
                        "MESSAGE": "User login successfully", "data": data.get("username")
                    },
                    status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            return Response(
                {
                    "MESSAGE": "Invalidate credentials ", "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST)
