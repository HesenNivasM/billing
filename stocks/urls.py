from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createStocks, name="createStocks"),
    path('update/', views.updateStocks, name="updateStocks"),
    path('view/', views.viewStocks, name="viewStocks"),
    path('', views.stocksPanel, name="stocksPanel" ),
]
