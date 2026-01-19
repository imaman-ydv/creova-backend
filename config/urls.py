from django.contrib import admin
from django.urls import path
from interest.views import home, submit_interest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('submit/', submit_interest, name='submit_interest'),
]
