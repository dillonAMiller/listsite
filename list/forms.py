from django import forms
from .models import Checklist
class itemDisplayedForm(forms.ModelForm):
            class Meta:
                model = Checklist.Set.Item
                fields = ('item_is_displayed',)

class popDisplayedForm(forms.ModelForm):
            class Meta:
                model = Checklist.Set.Pop
                fields = ('pop_is_displayed',)
        