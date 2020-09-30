from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class Item(models.Model):
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
    itemDisplayed = models.CharField(max_length=3, choices=item_is_displayed_choices, default='No')
    
    class itemDisplayedModel(models.Model):
        item_is_displayed_choices = (
            ('0', 'No'),
            ('1', 'Yes'),
    )
        itemDisplayed = models.CharField(max_length=3, choices=item_is_displayed_choices, default='No')
        def __str__(self):
            return self.itemDisplayed

    itemDisplayedtest = models.ManyToManyField(itemDisplayedModel)
class itemIsDisplayedForm(ModelForm):
    class Meta:
        model = Item.itemDisplayedModel
        fields = ['itemDisplayed']

class Pop(models.Model):
    pop_desc = models.CharField(max_length=20)
    objects = models.Manager()
    def __str__(self):
        return self.pop_desc

    pop_is_displayed_choices = (
        ('0', 'No'),
        ('1', 'Yes')
    )

    popDisplayed = models.CharField(max_length=3, choices=pop_is_displayed_choices, default='No')


class popIsDisplayedForm(ModelForm):
    class Meta:
        model = Pop
        fields = ['popDisplayed']

class Set(models.Model):
    set_name = models.CharField(max_length=200)
    objects = models.Manager()
    def __str__(self):
        return self.set_name

    items_in_set = models.ManyToManyField(Item)
    pop_in_set = models.ManyToManyField(Pop)

class Checklist(models.Model):
    store_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    objects = models.Manager()
    list_of_sets = models.ManyToManyField(Set)
    def __str__(self):
        return self.store_name

def is_displayed(item):
    if item.itemDisplayed == '0':
        item.itemDisplayed = '1'

def is_not_displayed(item):
    if item.itemDisplayed == '1':
        item.itemDisplayed = '0'

