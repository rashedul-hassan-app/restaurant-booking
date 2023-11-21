from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all, name='booking_page'),
    path('create/', views.create_booking, name='create_booking'),
    path('add_timeslot/', views.add_timeslot, name='add_timeslot'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking')
]
