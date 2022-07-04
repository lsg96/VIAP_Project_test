"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('faq/', views.FaqView.as_view(), name='faq'),
    path('information/', views.InfoView.as_view(), name='information'),
    path('review/', views.ReviewView.as_view(), name='review'),




]
