# Generated by Django 3.0.7 on 2020-07-07 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0006_pop_pop_is_displayed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_displayed',
        ),
    ]