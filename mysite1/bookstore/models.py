from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('name', max_length=64, default='', unique=True)
    pub = models.CharField('pub', max_length=100, default='')
    price = models.DecimalField('price', max_digits=7, decimal_places=2)
    info = models.CharField('info', max_length=100, default='',db_column='info')
    market_price = models.DecimalField('market_price', max_digits=7, decimal_places=2, default=0.0)
    test = models.DecimalField('test', max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField('is_active', default=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return '%s_%s_%s_%s_%s' % (self.title, self.pub, self.price, self.info, self.market_price)


class Author(models.Model):
    name = models.CharField('name', max_length=11, default='', null=False)
    age = models.IntegerField('age', default=1)
    email = models.EmailField('email', null=True)

    class Meta:
        db_table = 'author'
