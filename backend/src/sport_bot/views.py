from django.http import HttpResponse
from rest_framework import serializers, request, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models


# Create your views here.


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'first_name', 'username', 'gender', 'phone_number', 'current_standard']


class BotUsers(APIView):
    def get(self, request):
        all_users = models.User.objects.all()
        serializer = BotSerializer(all_users, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = BotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
