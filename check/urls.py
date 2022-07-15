"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('car_confirm/', views.Car_confirmView.as_view(), name='car_confirm'),
    path('pickup/', views.PickupView.as_view(), name='pickup'),
    path('car_info/', views.Car_infoView.as_view(), name='car_info'),
    path('car_apply/', views.Car_applyView.as_view(), name='car_apply'),
    path('car_alert/', views.Car_alertView.as_view(), name='car_alert'),
]
