from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blackjack_view, name='blackjack_view'),
]