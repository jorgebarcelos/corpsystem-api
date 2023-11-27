from django.db import models

# Create your models here.
class Sellers(models.Model):
    seller_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} {self.seller_id}"