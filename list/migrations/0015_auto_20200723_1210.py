# Generated by Django 3.0.7 on 2020-07-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0014_auto_20200723_1208'),
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
            field=models.CharField(choices=[('0', 'No'), ('1', 'Yes')], default='No', max_length=3),
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
