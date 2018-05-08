from django.urls import path, include

from pet import views

urlpatterns = [
    path('', views.index, name='index_pet'),
    path('query/<owner>', views.query_pet, name='query_pet'),
    path('registered/', views.registered, name='registered'),
]
