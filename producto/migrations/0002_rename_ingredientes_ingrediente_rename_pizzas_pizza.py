# Generated by Django 4.0 on 2021-12-11 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredientes',
            new_name='Ingrediente',
        ),
        migrations.RenameModel(
            old_name='Pizzas',
            new_name='Pizza',
        ),
    ]