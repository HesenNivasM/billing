from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createShops, name="createShops"),
    path('update/', views.updateShops, name="updateShops"),
    path('view/', views.viewShops, name="viewShops"),
    path('', views.shopsPanel, name="shopsPanel" ),
]
