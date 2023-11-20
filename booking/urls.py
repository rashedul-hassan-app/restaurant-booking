from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all, name='booking_page'),
    path('create/', views.create_booking, name='create_booking'),
    path('add_timeslot/', views.add_timeslot, name='add_timeslot'),
]
