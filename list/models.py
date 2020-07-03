from django.db import models

# Create your models here.



class item(models.Model):
    item_desc = models.CharField(max_length=100)
    item_vpn = models.CharField(max_length=10)
    item_crc = models.CharField(max_length=7)
    is_displayed_y_n = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    is_displayed = models.CharField(max_length=1, choices=is_displayed_y_n, default='0')
    
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

    def __str__(self):
        return self.pop_desc
    


class sets(models.Model):
    set_name = models.CharField(max_length=200)
    items_in_set = models.ManyToManyField(item)
    pop_in_set = models.ManyToManyField(pop)

    '''
    list_of_items = models.ForeignKey(
        item,
        on_delete=models.CASCADE)
    list_of_pop = models.ForeignKey(
        pop,
        on_delete=models.CASCADE)
    '''

    def __str__(self):
        return self.set_name

class Checklist(models.Model):
    store_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    list_of_sets = models.ManyToManyField(sets)

    def __str__(self):
        return self.store_name