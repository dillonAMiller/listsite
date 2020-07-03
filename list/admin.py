from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Checklist)
admin.site.register(models.item)
admin.site.register(models.pop)
admin.site.register(models.sets)

'''
is_displayed object changed to attribute
admin.site.register(models.item.is_displayed)
'''
