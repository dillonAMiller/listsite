from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
is_displayed_y_n = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    

class item(models.Model):
    item_desc = models.CharField(max_length=100)
    item_vpn = models.CharField(max_length=10)
    item_crc = models.CharField(max_length=7)
    '''

    from django.utils.translation import gettext_lazy as _
    class is_displayed(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')

        __empty__ = _('(Unknown')
    '''
    item_is_displayed_y_n = (
                ('0', 'No'),
                ('1', 'Yes'),
    )
    item_is_displayed = forms.ChoiceField(choices = item_is_displayed_y_n, label="Is Displayed", initial='', widget=forms.Select(), required=True)
    '''
    is_displayed = models.CharField(max_length=1, choices=is_displayed_y_n, default='0')
    '''
    '''
is_displayed_choices = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
class is_displayed(models.Model):
        
        displayed = models.ForeignKey(choices=is_displayed_choices, on_delete=models.CASCADE, )    
'''
    '''
    class is_displayedForm(forms.ModelForm):
        class Meta:
            model = is_displayed
            fields = ('displayed')
            widgets = {
                'displayed': forms.Select(choices=is_displayed_choices)
            }
    '''
    widget=forms.Select(choices=is_displayed_y_n)


    def __str__(self):
        return self.item_desc

    '''
    class is_displayed(models.Model):
        NO = 0, ('No')
        YES = 1, ('Yes')
        
        __empty__ = ('(Unknown)')
    '''


class pop(models.Model):
    pop_desc = models.CharField(max_length=20)
    pop_is_displayed_y_n = is_displayed_y_n = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    pop_is_displayed = models.CharField(max_length=1, choices=is_displayed_y_n, default='0')
    objects = models.Manager()
    def __str__(self):
        return self.pop_desc
    


class sets(models.Model):
    set_name = models.CharField(max_length=200)
    items_in_set = models.ManyToManyField(item)
    pop_in_set = models.ManyToManyField(pop)
    objects = models.Manager()
    def __str__(self):
        return self.set_name

    '''
    list_of_items = models.ForeignKey(
        item,
        on_delete=models.CASCADE)
    list_of_pop = models.ForeignKey(
        pop,
        on_delete=models.CASCADE)
    '''


class Checklist(models.Model):
    store_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    list_of_sets = models.ManyToManyField(sets)
    objects = models.Manager()

    def __str__(self):
        return self.store_name