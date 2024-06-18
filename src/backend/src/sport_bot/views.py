from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models


# Create your views here.


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'first_name', 'username', 'gender', 'phone_number']


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


class StandardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Standards
        fields = ['id', 'thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell', 'bench_press', 'axel_jerk',
                    'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk', 'taking_on_the_chest',
                    'axel_deadlift',
                    'classic_squat', 'front_squat', 'squat_over_the_head', 'back_squat', 'skipping_rope', 'push_ups',
                    'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump', 'holding_the_axel',
                    'handstand']


class StandardsUser(APIView):
    def get(self, requests):
        all_standards = models.Standards.objects.all()
        serializer = StandardsSerializer(all_standards, many=True)

        return Response(serializer.data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['id', 'training_history', 'number_of_referral_points', 'info_subscription', 'current_standard']


class ProfileUser(APIView):
    def get(self, requests):
        profile = models.Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, requests):
        serializer = ProfileSerializer(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



