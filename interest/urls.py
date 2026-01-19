from django.urls import path
from .views import home, submit_interest

urlpatterns = [
    path('', home),
    path('submit/', submit_interest),
]
