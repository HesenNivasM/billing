from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginToSite, name="loginToSite" ),
]