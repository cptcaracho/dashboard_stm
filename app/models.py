from django.db import models


# Create your models here.

class TestData1(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    revenue = models.DecimalField(max_digits=8, decimal_places=2)
    profit = models.DecimalField(max_digits=8, decimal_places=2)
    roi = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.cost} {self.revenue} {self.profit} {self.roi}"


class TestData2(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    revenue = models.CharField(max_length=255)
    profit = models.CharField(max_length=255)
    roi = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.cost} {self.revenue} {self.profit} {self.roi}"


class TestData3(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    revenue = models.CharField(max_length=255)
    profit = models.CharField(max_length=255)
    roi = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.cost} {self.revenue} {self.profit} {self.roi}"


class TestData4(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    revenue = models.CharField(max_length=255)
    profit = models.CharField(max_length=255)
    roi = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.cost} {self.revenue} {self.profit} {self.roi}"


class TestData5(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    revenue = models.CharField(max_length=255)
    profit = models.CharField(max_length=255)
    roi = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.cost} {self.revenue} {self.profit} {self.roi}"
