# Generated by Django 3.0.7 on 2020-07-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0013_auto_20200715_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='list_of_sets',
            field=models.ManyToManyField(to='list.Set'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemDisplayed',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3),
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