from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def str(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


# Create your models here.
