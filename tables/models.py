from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)\


    def __str__(self):
        return self.name


class Client(models.Model):
    client = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.ManyToManyField(Product)

    def __str__(self):
        return self.client, self.name


class Provider(models.Model):
    name = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
