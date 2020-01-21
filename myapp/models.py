from django.db import models


# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=50, unique=False)
    gender = models.CharField(max_length=10, unique=False)
    age = models.DateField()
    address = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    assignee_name = models.ForeignKey('Portfolio', on_delete=models.PROTECT)
    item_name = models.CharField(max_length=50, unique=False)
    assigned_date = models.DateField()
    returned_date = models.DateField()

    def __str__(self):
        return self.item_name


class Session(models.Model):
    name = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField()
    store_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.store_name
