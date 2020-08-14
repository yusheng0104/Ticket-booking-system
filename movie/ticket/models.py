from django.db import models

class Cinima(models.Model):
    name = models.CharField(max_length=64)
    zipcode = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.name}"

class Movies(models.Model):
    name = models.CharField(max_length=64)
    cinimaname = models.ManyToManyField(Cinima, blank=True, related_name="movies")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.name}"

class Coupon(models.Model):
    name = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.name}"
