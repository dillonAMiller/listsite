# Generated by Django 3.0.7 on 2020-07-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20200702_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='list_of_items',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='list_of_pop',
        ),
        migrations.CreateModel(
            name='sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=200)),
                ('items_in_set', models.ManyToManyField(to='list.item')),
                ('pop_in_set', models.ManyToManyField(to='list.pop')),
            ],
        ),
        migrations.AddField(
            model_name='checklist',
            name='list_of_sets',
            field=models.ManyToManyField(to='list.sets'),
        ),
    ]