from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price  = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.name
        # return f"id: {self.id} | name: {self.name}"