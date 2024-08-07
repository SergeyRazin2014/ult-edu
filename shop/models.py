from django.db import models

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tariff(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='tariffs')

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    discount_percentage = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    tariffs = models.ManyToManyField(Tariff, related_name='promotions')

    def __str__(self):
        return self.name
