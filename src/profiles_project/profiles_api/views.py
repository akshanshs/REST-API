from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """ test """

    def get(self, request, format=None):

        an_apiview = [
            'lol'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
        
