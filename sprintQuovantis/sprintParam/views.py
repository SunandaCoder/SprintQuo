import logging
from rest_framework.views import APIView
from sprintParam.serializers import SprintSerializer, ParamSerializer, VoteSerializer
from sprintParam.models import Parameter, Votes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from collections import Counter
from collections import defaultdict
from sprintParam.models import Sprint, Parameter
from sprintParam.utility import verify_token

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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @verify_token
    def get(self, request):
        """
        this method is created for retrieve data
        :param request: format of the request
        :return: Response
        """
        try:
            sprint = Sprint.objects.all()
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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @verify_token
    def put(self, request, id):
        """

        :param request: format of the request
        :param id: sprint id
        :return: response
        """
        print("hello")
        try:
            sprint = Sprint.objects.get(id=id)
            serializer = SprintSerializer(sprint, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Sprint updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK)
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "Sprint not updated"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "no such Sprint found",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @verify_token
    def delete(self, request, id):
        """
        This method is created for delete the existing data
        :param request: format of the request
        :param id: sprint id
        :return: Response
        """
        try:
            sprint = Sprint.objects.get(id=id)
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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class VotingParameter(APIView):
    """
    This class is created for parameter for particular sprint
    """

    @verify_token
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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @verify_token
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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @verify_token
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
                status=status.HTTP_200_OK)
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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @verify_token
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


class UserVote(APIView):
    """
    This class is creating for vote records
    """

    @verify_token
    def post(self, request, id):
        """
        this method is created for inserting the voting data
        :param sprint_id:
        :param request: format of the request
        :return: Response
        """

        try:

            sprint = {"sprint_id": id}
            vote_by = {"vote_by": request.data.get("user_id")}
            request_data = request.data.get("vote_table")
            for votes_dic in request_data:
                votes_dic.update(sprint)
                votes_dic.update(vote_by)
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
                        status=status.HTTP_400_BAD_REQUEST
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
                            status=status.HTTP_400_BAD_REQUEST
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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @verify_token
    def get(self, request, id):
        """
        this method is created for fetching the voting data
        :param id:
        :param vote_for:
        :param request: format of the request
        :return: Response
        """
        try:
            sprint_total = Votes.objects.filter(sprint_id=id,vote_by=request.data.get("user_id"))
            serializer = VoteSerializer(sprint_total, many=True)
            if serializer.data:
                votes_parameters = defaultdict(list)
                for vote_dic in serializer.data:
                    vote_by = vote_dic["vote_by"]
                    parameter_id = vote_dic["parameter_id"]
                    vote_for = vote_dic["vote_for"]
                    votes_parameters["vote_for:parameters"].append({vote_for: parameter_id})
                return Response(
                    {
                        "vote_by": vote_by,
                        "vote details": votes_parameters
                    },
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "message": " No Parameter for this user"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": " invalidate credentials"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @verify_token
    def put(self, request, id):
        """
        this method is update for using retrieve data
        :param sprint_id:
        :param request: format of the request
        :return: Response
        """
        try:
            sprint = {"sprint_id": id}
            vote_by = {"vote_by": request.data.get("user_id")}
            request_data = request.data.get("vote_table")
            for votes_dic in request_data:
                votes_dic.update(sprint)
                votes_dic.update(vote_by)
                votes_obj = Votes.objects.filter(
                    vote_by=votes_dic.get("vote_by"),
                    parameter_id=votes_dic.get("parameter_id"),
                    sprint_id=votes_dic.get("sprint_id")
                ).first()
                if votes_dic.get("vote_by") == votes_dic.get("vote_for"):
                    return Response(
                        {
                            "Message": "You Can not update your self parameter",
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
                else:
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
                status=status.HTTP_200_OK
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
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class Result(APIView):
    """
    This class Using for Voting Result
    """

    @verify_token
    def get(self, request, id):
        """
        this method is created for fetching the voting data
        :param sprint_id:
        :param request: format of the request
        :return: Response
        """
        try:
            sprint_total = Votes.objects.filter(sprint_id=id)
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
                status=status.HTTP_404_NOT_FOUND)
