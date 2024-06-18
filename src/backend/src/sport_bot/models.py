from django.db import models


# Create your models here.

class User(models.Model):
    GENDERS = [
        ('gen_men', 'Men'),
        ('gen_women', 'Women'),
    ]

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDERS, max_length=10)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return str(self.id) + " " + str(self.username) + " " + str(self.gender) + " " + str(self.phone_number)


class Standards(models.Model):
    id = models.IntegerField(primary_key=True)
    thunder = models.IntegerField(default=0)
    turkish_ascent_axel = models.IntegerField(default=0)
    turkish_ascent_kettlebell = models.IntegerField(default=0)
    bench_press = models.IntegerField(default=0)
    axel_jerk = models.IntegerField(default=0)
    taking_on_axel_chest = models.IntegerField(default=0)
    gluteal_bridge = models.IntegerField(default=0)
    deadlift = models.IntegerField(default=0)
    jerk = models.IntegerField(default=0)
    taking_on_the_chest = models.IntegerField(default=0)
    axel_deadlift = models.IntegerField(default=0)
    classic_squat = models.IntegerField(default=0)
    front_squat = models.IntegerField(default=0)
    squat_over_the_head = models.IntegerField(default=0)
    skipping_rope = models.IntegerField(default=0)
    push_ups = models.IntegerField(default=0)
    shuttle_running = models.IntegerField(default=0)
    farmer_walk = models.IntegerField(default=0)
    pull_ups = models.IntegerField(default=0)
    high_jump = models.IntegerField(default=0)
    long_jump = models.IntegerField(default=0)
    holding_the_axel = models.IntegerField(default=0)
    handstand = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + " " + "standards"


class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    training_history = models.TextField(default="-")
    number_of_referral_points = models.IntegerField(default=0)
    info_subscription = models.TextField(default="-")
    current_standard = models.TextField(default="-")

    def __str__(self):
        return (str(self.id) + " " + str(self.training_history) + " " + str(self.number_of_referral_points) + " "
                + str(self.info_subscription) + " " + str(self.current_standard))
