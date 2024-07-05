import datetime

from django.db import models
from django.urls import reverse

from src.db.router import cursor


# Create your models here.


class User(models.Model):
    telegram_id = models.IntegerField(default=89079009)
    first_name = models.CharField(max_length=50, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.telegram_id) + " " + str(self.first_name) + " " + "пользователь"


class Standards(User):
    thunder = models.IntegerField(default='0')
    turkish_ascent_axel = models.IntegerField(default='0')
    turkish_ascent_kettlebell = models.IntegerField(default='0')
    bench_press = models.IntegerField(default='0')
    axel_jerk = models.IntegerField(default='0')
    taking_on_axel_chest = models.IntegerField(default='0')
    gluteal_bridge = models.IntegerField(default='0')
    deadlift = models.IntegerField(default='0')
    jerk = models.IntegerField(default='0')
    taking_on_the_chest = models.IntegerField(default='0')
    axel_deadlift = models.IntegerField(default='0')
    classic_squat = models.IntegerField(default='0')
    front_squat = models.IntegerField(default='0')
    squat_over_the_head = models.IntegerField(default='0')
    skipping_rope = models.IntegerField(default='0')
    push_ups = models.IntegerField(default=0)
    shuttle_running = models.IntegerField(default='0')
    farmer_walk = models.IntegerField(default='0')
    pull_ups = models.IntegerField(default='0')
    high_jump = models.IntegerField(default='0')
    long_jump = models.IntegerField(default='0')
    holding_the_axel = models.IntegerField(default='0')
    handstand = models.IntegerField(default='0')

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
    username = models.CharField(max_length=50, default="")
    gender = models.CharField(choices=GENDERS, max_length=10, default='gender')
    phone_number = models.CharField(max_length=12, default="")
    training_history = models.TextField(default="-")
    number_of_referral_points = models.IntegerField(default=0)
    info_subscription = models.TextField(default="-")
    current_standard = models.TextField(default="-")

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

    dynamic_id = cursor.lastrowid + 1

    user_id = models.IntegerField(default=89898989)
    user_name = models.TextField(max_length=20, default='')

    thunder = models.IntegerField(default='0')
    turkish_ascent_axel = models.IntegerField(default='0')
    turkish_ascent_kettlebell = models.IntegerField(default='0')
    bench_press = models.IntegerField(default='0')
    axel_jerk = models.IntegerField(default='0')
    taking_on_axel_chest = models.IntegerField(default='0')
    gluteal_bridge = models.IntegerField(default='0')
    deadlift = models.IntegerField(default='0')
    jerk = models.IntegerField(default='0')
    taking_on_the_chest = models.IntegerField(default='0')
    axel_deadlift = models.IntegerField(default='0')
    classic_squat = models.IntegerField(default='0')
    front_squat = models.IntegerField(default='0')
    squat_over_the_head = models.IntegerField(default='0')
    skipping_rope = models.IntegerField(default='0')
    push_ups = models.IntegerField(default=0)
    shuttle_running = models.IntegerField(default='0')
    farmer_walk = models.IntegerField(default='0')
    pull_ups = models.IntegerField(default='0')
    high_jump = models.IntegerField(default='0')
    long_jump = models.IntegerField(default='0')
    holding_the_axel = models.IntegerField(default='0')
    handstand = models.IntegerField(default='0')
    dynamic_month = datetime.datetime.now().month
    dynamic_year = datetime.datetime.now().year

    month = models.TextField(choices=months, default=definition_month(str(dynamic_month)))
    year = models.TextField(default=dynamic_year)

    def __str__(self):
        return str(self.user_id) + " " + "статистика"


class StatisticsGet(models.Model):
    dynamic_year = datetime.datetime.now().year

    standard = models.TextField(default='')
    year = models.TextField(default=dynamic_year)

    def __str__(self):
        return str(self.standard) + " " + str(self.year)


class LoginUser(models.Model):
    username = models.TextField(default='')
    password = models.TextField(default='')

    def __str__(self):
        return str(self.username) + " " + str(self.password)
