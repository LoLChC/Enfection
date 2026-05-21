from . import views
from django.urls import path

urlpatterns = [
    path('', views.trikinoz, name="home"),
    path('/trikinoz', views.home, name="trikinoz")
]
