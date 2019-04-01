from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createBill, name="createBill" ),
    path('view/', views.viewBill, name="viewBill" ),
    path('', views.billPanel, name="billPanel" ),
]
