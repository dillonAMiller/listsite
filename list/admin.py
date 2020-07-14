from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Checklist)
admin.site.register(models.Checklist.Set.Item)
admin.site.register(models.Checklist.Set.Pop)
admin.site.register(models.Checklist.Set)
