# Generated by Django 3.0.7 on 2020-07-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0011_auto_20200714_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='list_of_sets',
            field=models.ManyToManyField(to='list.Set'),
        ),
        migrations.AlterField(
            model_name='set',
            name='items_in_set',
            field=models.ManyToManyField(to='list.Item'),
        ),
        migrations.AlterField(
            model_name='set',
            name='pop_in_set',
            field=models.ManyToManyField(to='list.Pop'),
        ),
    ]