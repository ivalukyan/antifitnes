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
    thunder = models.CharField(max_length=50)
    turkish_ascent_axel = models.CharField(max_length=50)
    turkish_ascent_kettlebell = models.CharField(max_length=50)
    bench_press = models.CharField(max_length=50)
    axel_jerk = models.CharField(max_length=50)
    taking_on_axel_chest = models.CharField(max_length=50)
    gluteal_bridge = models.CharField(max_length=50)
    deadlift = models.CharField(max_length=50)
    jerk = models.CharField(max_length=50)
    taking_on_the_chest = models.CharField(max_length=50)
    axel_deadlift = models.CharField(max_length=50)
    classic_squat = models.CharField(max_length=50)
    front_squat = models.CharField(max_length=50)
    squat_over_the_head = models.CharField(max_length=50)
    back_squat = models.CharField(max_length=50)
    skipping_rope = models.CharField(max_length=50)
    push_ups = models.CharField(max_length=50)
    shuttle_running = models.CharField(max_length=50)
    farmer_walk = models.CharField(max_length=50)
    pull_ups = models.CharField(max_length=50)
    high_jump = models.CharField(max_length=50)
    long_jump = models.CharField(max_length=50)
    holding_the_axel = models.CharField(max_length=50)
    handstand = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + " " + "standards"


class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    training_history = models.TextField()
    number_of_referral_points = models.IntegerField()
    info_subscription = models.TextField()
    current_standard = models.TextField(default="No standard")

    def __str__(self):
        return (str(self.id) + " " + str(self.training_history) + " " + str(self.number_of_referral_points) + " "
                + str(self.info_subscription) + " " + str(self.current_standard))
