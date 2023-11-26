from django.urls import path
from customers.api.api import api

urlpatterns = [
    path('', api.urls)
]
