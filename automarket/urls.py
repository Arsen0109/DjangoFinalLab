from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]