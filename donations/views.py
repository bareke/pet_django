from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .models import FoodSupply, VolunteerService


class initialDonationView(TemplateView):
    template_name = 'landing_donation.html'

class foodCreateView(CreateView):
    model = FoodSupply
    fields = ['food_type', 'quantity', 'email', 'delivery_time', 'name']
    success_url = '../'

class volunteerCreateView(CreateView):
    model = VolunteerService
    fields = ['volunteer_type', 'email', 'delivery_time', 'name']
    success_url = '../'
