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
    thunder = models.TextField(default="-")
    turkish_ascent_axel = models.TextField(default="-")
    turkish_ascent_kettlebell = models.TextField(default="-")
    bench_press = models.TextField(default="-")
    axel_jerk = models.TextField(default="-")
    taking_on_axel_chest = models.TextField(default="-")
    gluteal_bridge = models.TextField(default="-")
    deadlift = models.TextField(default="-")
    jerk = models.TextField(default="-")
    taking_on_the_chest = models.TextField(default="-")
    axel_deadlift = models.TextField(default="-")
    classic_squat = models.TextField(default="-")
    front_squat = models.TextField(default="-")
    squat_over_the_head = models.TextField(default="-")
    skipping_rope = models.TextField(default="-")
    push_ups = models.TextField(default="-")
    shuttle_running = models.TextField(default="-")
    farmer_walk = models.TextField(default="-")
    pull_ups = models.TextField(default="-")
    high_jump = models.TextField(default="-")
    long_jump = models.TextField(default="-")
    holding_the_axel = models.TextField(default="-")
    handstand = models.TextField(default="-")

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
