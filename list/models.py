from django.db import models

# Create your models here.

class Checklist(models.Model):
    store_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class item(models.Model):
    item_desc = models.CharField(max_length=100)
    item_vpn = models.CharField(max_length=10)
    item_crc = models.CharField(max_length=7)
'''
    class is_displayed(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')
        
        __empty__ = _('(Unknown)')
'''
class pop(models.Model):
    pop_desc = models.CharField(max_length=20)

