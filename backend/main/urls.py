from django.urls import path
from main import views

urlpatterns = [
    path('getRandomCapitalCity/', views.getRandomCapitalCity, name='getRandomCapitalCity'),
    path('checkCapital/', views.checkCapital, name='checkCapital'),
]