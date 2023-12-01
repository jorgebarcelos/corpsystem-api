from django.urls import path
from sellers.api.api import api

urlpatterns = [
    path('', api.urls)
]
