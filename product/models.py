from django.db import models
from django.forms import DecimalField

class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # def get_average_rating(self):
    #     ratings = [rating.value for rating in self.ratings.all()]
    #     if ratings:
    #         return sum(ratings)/len(ratings)
    #     else:
    #         return 0