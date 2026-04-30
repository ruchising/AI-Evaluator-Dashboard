from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_evaluation, name='submit'),
    path('dashboard/', views.dashboard, name='dashboard'),
]