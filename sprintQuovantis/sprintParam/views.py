import json
import logging
from rest_framework.views import APIView
from sprintParam.serializers import SprintSerializer, ParamSerializer, VoteSerializer
from sprintParam.models import Parameter, Votes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

logging.basicConfig(filename="views.log", filemode="w")


class Sprint(APIView):
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
                    "message": "Data store successfully",
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
            sprint = Sprint.objects.filter(Sprint_id=request.data.get("Sprint_id"))
            serializer = SprintSerializer(sprint, many=True)
            return Response(
                {
                    "message": "Here your sprint",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            logging.error(e)
            return Response(
                {
                    "message": "No notes for you"
                },
                status=status.HTTP_400_BAD_REQUEST)


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
                    "message": "Data store successfully",
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


class UserVote(APIView):
    """
    This class is creating for vote records
    """
    def post(self, request):
        """
        this method is created for inserting the voting data
        :param request: format of the request
        :return: Response
        """
        try:
            serializer = VoteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "Message": "User Vote Successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        except ValidationError:
            logging.error("Validation Failed")
            return Response(
                {
                    "Message": "Validation Failed"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "Message": "Invalid User"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class Result(APIView):
    """
    This class Using for Voting Result
    """

    def get(self, request):
        """
        this method is created for fetching the voting data
        :param request: format of the request
        :return: Response
        """
        try:
            votes = Votes.objects.filter(vote_for=request.data.get("vote_for"))
            for i in votes:
                print(i.parameter_id)

            return Response(
                {
                    "message": "Total votes ",
                    "Votes": len(list(i for i in votes))
                },
                status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            logging.error(e)
            return Response(
                {
                    "message": " No Parameter for you"
                },
                status=status.HTTP_400_BAD_REQUEST)


