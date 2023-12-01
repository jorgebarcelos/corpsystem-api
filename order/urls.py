from django.urls import path
from order.api.api import api

urlpatterns = [
    path('', api.urls)
]
