from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class TestEndpoint(APIView):
    def get(self, request):
        return Response({"test" : "1"})