# Generated by Django 2.2.12 on 2021-11-22 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='author',
            new_name='user',
        ),
    ]
