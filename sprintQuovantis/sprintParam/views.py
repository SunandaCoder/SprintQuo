import json
import logging
from rest_framework.views import APIView
from sprintParam.serializers import SprintSerializer, ParamSerializer, VoteSerializer
from sprintParam.models import Parameter, Votes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from collections import Counter
from collections import defaultdict

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

    def post(self, request, sprint_id=None):
        """
        this method is created for inserting the voting data
        :param sprint_id:
        :param request: format of the request
        :return: Response
        """

        try:
            sprint = {"sprint_id": sprint_id}
            request_data = request.data
            for votes_dic in request_data:
                votes_dic.update(sprint)
                votes_obj = Votes.objects.filter(
                    vote_by=votes_dic.get("vote_by"),
                    parameter_id=votes_dic.get("parameter_id"),
                    sprint_id=votes_dic.get("sprint_id")
                ).first()
                if votes_dic.get("vote_by") == votes_dic.get("vote_for"):
                    return Response(
                        {
                            "Message": "You Can not vote your self",
                        },
                        status=status.HTTP_201_CREATED
                    )
                else:
                    if votes_obj is None:
                        serializer = VoteSerializer(
                            data=votes_dic
                        )
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                    else:
                        return Response(
                            {"Message": "User already vote this parameter please choice another one"},
                            status=status.HTTP_302_FOUND
                        )
                return Response(
                    {
                        "Message": "User Vote Successfully",
                        "data": request_data
                    },
                    status=status.HTTP_201_CREATED
                )
        except ValidationError:
            logging.error("Validation Failed")
            return Response(
                {
                    "Message": "Enter Validate credentials"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "Message": "Enter all credentials"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, sprint_id, user_id):
        """
        this method is created for fetching the voting data
        :param user_id:
        :param sprint_id:
        :param request: format of the request
        :return: Response
        """
        try:
            sprint_total = Votes.objects.filter(sprint_id=sprint_id, vote_for=user_id).all()
            serializer = VoteSerializer(sprint_total, many=True)
            if serializer.data:
                votes_parameters = defaultdict(list)
                for vote_dic in serializer.data:
                    vote_for = vote_dic["vote_for"]
                    parameter_id = vote_dic["parameter_id"]
                    vote_by = vote_dic["vote_by"]
                    votes_parameters["user_id"] = vote_for
                    votes_parameters["parameters"].append({vote_by: parameter_id})
                return Response(
                    {
                        "vote details": votes_parameters
                    },
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "message": " No Parameter for this user"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": " invalidate credentials"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, sprint_id):
        """
        this method is update for using retrieve data
        :param sprint_id:
        :param request: format of the request
        :return: Response
        """
        try:
            sprint = {"sprint_id": sprint_id}
            request_data = request.data
            for votes_dic in request_data:
                votes_dic.update(sprint)
                votes_obj = Votes.objects.filter(
                    vote_by=votes_dic.get("vote_by"),
                    parameter_id=votes_dic.get("parameter_id"),
                    sprint_id=votes_dic.get("sprint_id")
                ).first()
                if votes_obj is None:
                    serializer = VoteSerializer(instance=votes_obj, data=votes_dic)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                else:
                    votes_obj.delete()
                    serializer = VoteSerializer(data=votes_dic)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

            return Response(
                {
                    "Message": "Update data Successfully ",
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
                    "message": "invalidate credentials"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class Result(APIView):
    """
    This class Using for Voting Result
    """

    def get(self, request, sprint_id):
        """
        this method is created for fetching the voting data
        :param sprint_id:
        :param request: format of the request
        :return: Response
        """
        try:
            sprint_total = Votes.objects.filter(sprint_id=sprint_id)
            serializer = VoteSerializer(sprint_total, many=True)
            vote_list = []
            for vote_dic in serializer.data:
                vote_for = vote_dic["vote_for"]
                vote_list.append(vote_for)
            vote_count = Counter(vote_list)
            winner = max(vote_count, key=lambda x: vote_count[x])
            return Response(
                {
                    "winner is": winner,
                    "vote index": vote_count,
                    "vote details": serializer.data
                },
                status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": " No Parameter for you"
                },
                status=status.HTTP_400_BAD_REQUEST)
