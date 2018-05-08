from django.urls import path, include
import donations.views as donation_views

urlpatterns = [
    path('', donation_views.initialDonationView.as_view(), name='index_donation'),
    path('donate-food/', donation_views.foodCreateView.as_view(), name='food_donation'),
    path('donate-volunteer/', donation_views.volunteerCreateView.as_view(), name='volunteers_donation'),

]
