from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/consultation/', views.send_consultation, name='submit_consultation'),
]

