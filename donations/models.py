from django.db import models
from .model_choices import FOOD_TYPES, VOLUNTEER_TYPE


class HumanUser(models.Model):
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='human_profile_img', blank=True)

    def __str__(self):
        return '{0.email}'.format(self)


class AbsctractDonation(models.Model):
    user = models.ForeignKey(HumanUser, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()

    class Meta:
        abstract = True


class FoodSupply(AbsctractDonation):
    food_type = models.CharField(max_length=20, choices=FOOD_TYPES)
    quantity = models.FloatField()

    def __str__(self):
        return '{0.name} {0.food_type} on {0.delivery_time}'.format(self)


class VolunteerService(AbsctractDonation):
    volunteer_type = models.CharField(max_length=20, choices=VOLUNTEER_TYPE)

    def __str__(self):
        return '{0.name} {0.volunteer_type} on {0.delivery_time}'.format(self)
