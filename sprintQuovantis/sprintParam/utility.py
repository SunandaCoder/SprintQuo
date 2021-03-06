from rest_framework.response import Response
from django.http import QueryDict
from user.utils import EncodeDecodeToken
import logging


def verify_token(function):
    """
    this function is created for verifying user
    """

    def wrapper(self, request, id=None):
        if 'HTTP_AUTHORIZATION' not in request.META:
            resp = Response({'message': 'Token not provided in the header'})
            resp.status_code = 400
            logging.info('Token not provided in the header')
            return resp
        token = request.META['HTTP_AUTHORIZATION']
        user_id = EncodeDecodeToken.decode_token(token)
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data.update({'user_id': user_id["user_id"]})
        if id:
            return function(self, request, id)
        return function(self, request)

    return wrapper
