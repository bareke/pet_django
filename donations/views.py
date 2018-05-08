from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView
from .models import FoodSupply, VolunteerService


class initialDonationView(FormView):
    template_name = 'landing_donation.html'
    success_url = ''

class foodCreateView(CreateView):
    model = FoodSupply
    fields = ['food_type', 'quantity', 'email', 'delivery_time', 'name']
    success_url = '../'

class volunteerCreateView(CreateView):
    model = VolunteerService
    fields = ['volunteer_type', 'email', 'delivery_time', 'name']
    success_url = '../'
