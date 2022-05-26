from django.urls import path

from playground import views

urlpatterns = [
    path('health/', views.health_check),
]