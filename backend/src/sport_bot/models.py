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
    current_standard = models.CharField(max_length=500)

    def __str__(self):
        return str(self.id) + " " + str(self.username) + " " + str(self.gender) + " " + str(self.phone_number) + " " + str(self.current_standard)

