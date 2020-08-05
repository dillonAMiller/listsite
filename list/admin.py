from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Checklist)
admin.site.register(models.Item)
admin.site.register(models.Item.itemDisplayedModel)
admin.site.register(models.Pop)
admin.site.register(models.Set)
