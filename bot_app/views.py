from django.http import HttpResponseRedirect
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import DetailView

from bot_app.models import Standards, Statistics
from src.db.db_standards import get_names_standards
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect

from bot_app import models
from bot_app.forms import StandardsForm, StatisticsForm


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'first_name']


class BotUsers(APIView):
    def get(self, request):
        all_users = models.User.objects.all()
        serializer = BotSerializer(all_users, many=True)

        return Response(serializer.data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['id', 'first_name', 'username', 'gender', 'phone_number', 'training_history',
                  'number_of_referral_points', 'info_subscription', 'current_standard']


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


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statistics
        fields = ['id', 'user_id', 'user_name', 'thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell',
                  'bench_press',
                  'axel_jerk', 'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk', 'taking_on_the_chest',
                  'axel_deadlift', 'classic_squat', 'front_squat', 'squat_over_the_head', 'skipping_rope',
                  'push_ups', 'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump',
                  'holding_the_axel',
                  'handstand', 'month', 'year']


class StatisticsUser(APIView):
    def get(self, requests):
        statistics = models.Statistics.objects.all()
        serializer = StatisticsSerializer(statistics, many=True)
        return Response(serializer.data)


def index(requests):
    return render(requests, 'index.html', status=200)


def standards_create(requests):
    if requests.method == 'POST':
        form = StandardsForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)

    form = StandardsForm()

    data = {'form': form}

    return render(requests, 'createstandards.html', data)


# def standards_id(requests, pk):
#     data = models.Standards.objects.get(id=pk)
#     print(data)
#     arg = {'data': data}
#     return render(requests, 'standards_id.html', arg)

class StandardsID(DetailView):
    model = Standards
    template_name = 'standards_id.html'
    context_object_name = 'standard'


def standards(requests):
    if requests.method == 'GET':
        data = models.Standards.objects.all()
        arg = {'data': data}

        return render(requests, 'standards.html', arg)


def statistics(requests):

    data = models.Statistics.objects.all()
    arg = {'data': data}
    return render(requests, 'statistics.html', arg)


def createstatistics(requests):

    if requests.method == 'POST':
        form = StatisticsForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)

    form = StatisticsForm()

    data = {'form': form}

    return render(requests, 'createstatistics.html', data)


class StatisticsID(DetailView):
    model = Statistics
    template_name = 'statistic_id.html'
    context_object_name = 'stat'


def profile(requests):
    if requests.method == 'GET':
        data = models.Profile.objects.all()
        arg = {'data': data}
        return render(requests, 'profile.html', arg)
