# Generated by Django 3.0.7 on 2020-06-30 16:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='list_of_items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='list.item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checklist',
            name='list_of_pop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='list.pop'),
            preserve_default=False,
        ),
    ]
