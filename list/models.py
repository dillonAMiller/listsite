from django.db import models

# Create your models here.



class item(models.Model):
    item_desc = models.CharField(max_length=100)
    item_vpn = models.CharField(max_length=10)
    item_crc = models.CharField(max_length=7)

    def __str__(self):
        return self.item_desc


    class is_displayed(models.IntegerChoices):
        NO = 0, ('No')
        YES = 1, ('Yes')
        
        __empty__ = ('(Unknown)')

class pop(models.Model):
    pop_desc = models.CharField(max_length=20)

    def __str__(self):
        return self.pop_desc

class Checklist(models.Model):
    store_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    list_of_items = models.ForeignKey(
        item,
        on_delete=models.CASCADE)
    list_of_pop = models.ForeignKey(
        pop,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name