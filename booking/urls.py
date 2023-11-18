from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all, name='booking_page'),
]
