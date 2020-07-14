from django.db import models

from django import forms

# Create your models here.
class Checklist(models.Model):
    store_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    objects = models.Manager()

    def __str__(self):
        return self.store_name

    class set(models.Model):
        set_name = models.CharField(max_length=200)
        objects = models.Manager()
        def __str__(self):
            return self.set_name

        class item(models.Model):
            item_desc = models.CharField(max_length=100)
            item_vpn = models.CharField(max_length=10)
            item_crc = models.CharField(max_length=7)
            objects = models.Manager()

            def __str__(self):
                return self.item_desc

            item_is_displayed_choices = (
                    ('0', 'No'),
                    ('1', 'Yes'),
            )

            item_is_displayed = models.CharField(max_length=3, choices=item_is_displayed_choices, default='No')

        class pop(models.Model):
            pop_desc = models.CharField(max_length=20)
            objects = models.Manager()
            def __str__(self):
                return self.pop_desc

            pop_is_displayed_choices = (
                ('0', 'No'),
                ('1', 'Yes')
            )

            pop_is_displayed = models.CharField(max_length=3, choices=pop_is_displayed_choices, default='No')

        items_in_set = models.ManyToManyField(item)
        pop_in_set = models.ManyToManyField(pop)
    list_of_sets = models.ManyToManyField(set)