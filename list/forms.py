from django import forms
from .models import Checklist
class itemDisplayedForm(forms.ModelForm):
            class Meta:
                model = Checklist.set.item
                fields = ('item_is_displayed',)

class popDisplayedForm(forms.ModelForm):
            class Meta:
                model = Checklist.set.pop
                fields = ('pop_is_displayed',)
        