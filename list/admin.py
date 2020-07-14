from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Checklist)
admin.site.register(models.Checklist.set.item)
admin.site.register(models.Checklist.set.pop)
admin.site.register(models.Checklist.set)
