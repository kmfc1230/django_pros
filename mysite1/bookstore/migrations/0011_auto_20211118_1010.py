# Generated by Django 2.2.12 on 2021-11-18 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0010_auto_20211118_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
    ]
