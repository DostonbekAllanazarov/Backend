from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('topic/', views.topic, name="topic"),
    path('room/<int:id>/', views.room, name="room"),
]
