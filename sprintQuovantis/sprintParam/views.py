import logging
from rest_framework.views import APIView
from sprintParam.serializers import SprintSerializer, ParamSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from sprintParam.models import Sprint, Parameter
from django.views.decorators.csrf import csrf_exempt

logging.basicConfig(filename="views.log", filemode="w")


class SprintQuo(APIView):
    """
    This class is created for Sprint
    """

    def post(self, request):
        """
        this method is created for inserting the data
        :param request: format of the request
        :return: Response
        """
        try:
            serializer = SprintSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Sprint store successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED)
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
                    "message": "Data not stored"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        this method is created for retrieve data
        :param request: format of the request
        :return: Response
        """
        try:
            sprint = Sprint.objects.filter(id=request.data.get("id"))
            serializer = SprintSerializer(sprint, many=True)
            return Response(
                {
                    "message": "Here your sprint",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            logging.error(e)
            return Response(
                {
                    "message": "No sprint for you"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        this method is created for update the data
        :param request: format of the request
        :return: Response
        """
        try:
            sprint = Sprint.objects.get(id=request.data["id"])
            serializer = SprintSerializer(sprint, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Sprint updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_202_ACCEPTED)
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "Sprint not updated"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(e)
            print(e)
            return Response(
                {
                    "message": "no such Sprint found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request):
        """
        This method is created for delete the existing data
        :param request: format of the request
        :return: Response
        """
        try:
            sprint = Sprint.objects.get(id=request.data["id"])
            sprint.delete()
            return Response(
                {
                    "message": "Sprint deleted successfully"
                },
                status=status.HTTP_200_OK)
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "Sprint not deleted"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "no such sprint found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class ParameterOfSprint(APIView):
    """
    This class is created for parameter for particular sprint
    """

    def post(self, request):
        """
        this method is created for inserting the data
        :param request: format of the request
        :return: Response
        """
        try:
            serializer = ParamSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Parameter store successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED)
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
                    "message": "Parameter not stored"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        this method is created for fetching the data
        :param request: format of the request
        :return: Response
        """
        try:
            para = Parameter.objects.all()
            serializer = ParamSerializer(para, many=True)
            return Response(
                {
                    "message": "Here your parameter",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "No parameter to show"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        this method is created for update the existing data
        :param request: format of the request
        :return: Response
        """
        try:
            para = Parameter.objects.get(id=request.data["id"])
            serializer = ParamSerializer(para, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "parameter updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_202_ACCEPTED)
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "Parameter not updated"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "no such parameter found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request):
        """
        This method is created for delete the existing data
        :param request: format of the request
        :return: Response
        """
        try:
            para = Parameter.objects.get(id=request.data["id"])
            para.delete()
            return Response(
                {
                    "message": "Parameter deleted successfully"
                },
                status=status.HTTP_200_OK)
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "Parameter not deleted"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "no such parameter found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

