# Generated by Django 3.0.7 on 2020-07-16 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0012_auto_20200715_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_is_displayed',
            new_name='itemDisplayed',
        ),
        migrations.RenameField(
            model_name='pop',
            old_name='pop_is_displayed',
            new_name='popDisplayed',
        ),
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
