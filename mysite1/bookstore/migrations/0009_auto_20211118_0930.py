# Generated by Django 2.2.12 on 2021-11-18 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0008_auto_20211118_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='test',
            field=models.CharField(default='', max_length=50, verbose_name='测试'),
        ),
    ]