# Generated by Django 3.0.7 on 2020-08-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0018_auto_20200805_0658'),
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