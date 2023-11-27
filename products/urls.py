from django.urls import path
from products.api.api import api

urlpatterns = [
    path('', api.urls)
]
