# Generated by Django 4.2.7 on 2023-11-07 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_exist',
        ),
    ]
