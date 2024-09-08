from django.urls import path
from . import views
from .views import pandit_register

urlpatterns = [
    path('', views.pandit_list, name = 'pandit_list'),
    path('users/', views.user_list, name = 'users_list'),
    path('bookings/', views.booking_list, name = 'booking_list'),
    path('register/', pandit_register, name='pandit_register'),
]
