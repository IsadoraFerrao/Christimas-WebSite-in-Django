from django.urls import path
from.import views 

urlpatterns = [
    path('', views.home, name="natalFeliz-home"),
    path('about/', views.about, name="natalFeliz-about"),
]
