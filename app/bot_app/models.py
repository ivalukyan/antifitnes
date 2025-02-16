import datetime
from uuid import uuid4

from django.db import models
from django.urls import reverse


# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    telegram_id = models.BigIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.telegram_id) + " " + str(self.first_name) + " " + "пользователь"


class Standards(User):
    thunder = models.FloatField(default='0')
    turkish_ascent_axel = models.FloatField(default='0')
    turkish_ascent_kettlebell = models.FloatField(default='0')
    bench_press = models.FloatField(default='0')
    axel_jerk = models.FloatField(default='0')
    taking_on_axel_chest = models.FloatField(default='0')
    gluteal_bridge = models.FloatField(default='0')
    deadlift = models.FloatField(default='0')
    jerk = models.FloatField(default='0')
    taking_on_the_chest = models.FloatField(default='0')
    axel_deadlift = models.FloatField(default='0')
    classic_squat = models.FloatField(default='0')
    front_squat = models.FloatField(default='0')
    squat_over_the_head = models.FloatField(default='0')
    skipping_rope = models.FloatField(default='0')
    push_ups = models.FloatField(default=0)
    shuttle_running = models.FloatField(default='0')
    farmer_walk = models.FloatField(default='0')
    pull_ups = models.FloatField(default='0')
    high_jump = models.FloatField(default='0')
    long_jump = models.FloatField(default='0')
    holding_the_axel = models.FloatField(default='0')
    handstand = models.FloatField(default='0')

    def __str__(self):
        return str(self.telegram_id) + "нормативы"

    def get_absolute_url(self):
        return reverse('standards_id', kwargs={'slug': self.slug})


class Profile(User):
    GENDERS = [
        ('gen_men', 'Мужской'),
        ('gen_women', 'Женский'),
        ('gender', 'Неизвестно')
    ]
    username = models.CharField(max_length=50, default="", blank=True, null=True)
    gender = models.CharField(choices=GENDERS, max_length=10, default='gender')
    phone_number = models.CharField(max_length=12, default="")
    training_history = models.TextField(default="-", blank=True, null=True)
    number_of_referral_points = models.TextField(default="Реферальные баллы отсутствуют", blank=True, null=True)
    info_subscription = models.TextField(default="-", blank=True, null=True)
    current_standard = models.TextField(default="-", blank=True, null=True)
    telegram_status = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.phone_number) + " " + "профиль пользователя"


def definition_month(month):
    if month in ['1', '2', '3']:
        return '1'
    elif month in ['4', '5', '6']:
        return '4'
    elif month in ['7', '8', '9']:
        return '7'
    elif month in ['10', '11', '12']:
        return '10'


class Statistics(models.Model):
    months = [
        ('1', 'Январь'),
        ('4', 'Апрель'),
        ('7', 'Июль'),
        ('10', 'Октябрь')
    ]

    id = models.UUIDField(primary_key=True, default=uuid4)
    user_id = models.BigIntegerField(default=89898989)
    user_name = models.TextField(max_length=20, default='')

    thunder = models.FloatField(default='0', null=True)
    turkish_ascent_axel = models.FloatField(default='0', null=True)
    turkish_ascent_kettlebell = models.FloatField(default=0, null=True)
    bench_press = models.FloatField(default=0, null=True)
    axel_jerk = models.FloatField(default=0, null=True)
    taking_on_axel_chest = models.FloatField(default=0, null=True)
    gluteal_bridge = models.FloatField(default=0, null=True)
    deadlift = models.FloatField(default=0, null=True)
    jerk = models.FloatField(default=0, null=True)
    taking_on_the_chest = models.FloatField(default=0, null=True)
    axel_deadlift = models.FloatField(default=0, null=True)
    classic_squat = models.FloatField(default=0, null=True)
    front_squat = models.FloatField(default=0, null=True)
    squat_over_the_head = models.FloatField(default=0, null=True)
    skipping_rope = models.FloatField(default=0, null=True)
    push_ups = models.FloatField(default=0, null=True)
    shuttle_running = models.FloatField(default=0, null=True)
    farmer_walk = models.FloatField(default=0, null=True)
    pull_ups = models.FloatField(default=0, null=True)
    high_jump = models.FloatField(default=0, null=True)
    long_jump = models.FloatField(default=0, null=True)
    holding_the_axel = models.FloatField(default=0, null=True)
    handstand = models.FloatField(default=0, null=True)
    dynamic_month = datetime.datetime.now().month
    dynamic_year = datetime.datetime.now().year

    month = models.TextField(choices=months, default=definition_month(str(dynamic_month)))
    year = models.TextField(default=dynamic_year)

    def __str__(self):
        return str(self.user_id) + " " + "статистика"


class LoginUser(models.Model):
    username = models.TextField(default='')
    password = models.TextField(default='')

    def __str__(self):
        return str(self.username) + " " + str(self.password)


# class CRMInfo(models.Model):
#     pass
