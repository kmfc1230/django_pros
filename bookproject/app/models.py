from django.db import models


# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=64, null=False)
    address = models.CharField(verbose_name='地址', max_length=64, null=False)


class Book(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=32, null=False)
    price = models.DecimalField(verbose_name='价格', max_digits=5, decimal_places=2, default=10.01)
    inventory = models.IntegerField(verbose_name='库存数')
    sale_num = models.IntegerField(verbose_name='卖出数')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class Author(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=32)
    book = models.ManyToManyField(Book)
