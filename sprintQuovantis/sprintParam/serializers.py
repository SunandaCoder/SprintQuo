from rest_framework import serializers
from sprintParam.models import Votes
from sprintParam.models import Sprint, Parameter


class SprintSerializer(serializers.ModelSerializer):
    """
    Serializer is used to converting the python object for the Sprint
    """

    class Meta:
        model = Sprint
        fields = "__all__"

    def create(self, validate_data):
        """
        for creating the sprint
        :param validate_data:  validate the api data
        :return: sprint
        """
        sprint = Sprint.objects.create(
            sprint_name=validate_data.get("sprint_name"),
            entry_date=validate_data.get("entry_date"),
            expiry_date=validate_data.get("expiry_date")
        )
        return sprint


class ParamSerializer(serializers.ModelSerializer):
    """
    Serializer is used to converting the python object for the Parameter
    """

    class Meta:
        model = Parameter
        fields = "__all__"

    def create(self, validate_data):
        """
        for creating the parameter
        :param validate_data: validating the api data
        :return: Parameter
        """
        parameter = Parameter.objects.create(
            parameter_name=validate_data.get("parameter_name"),
        )
        return parameter


class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer is user to converting the python object for the Vote
    """
    class Meta:
        model = Votes
        fields = "__all__"

    def create(self, validated_data):
        """
        for the votes operations
        :param validated_data: validating the api data
        :return: vote
        """
        vote = Votes.objects.create(
            sprint_id=validated_data.get("sprint_id"),
            parameter_id=validated_data.get("parameter_id"),
            vote_by=validated_data.get("vote_by"),
            vote_for=validated_data.get("vote_for"),
        )

        return vote
