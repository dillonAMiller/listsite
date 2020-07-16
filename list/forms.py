from django import forms
from .models import Checklist, Set, Item, Pop
class itemDisplayedForm(forms.ModelForm):
            class Meta:
                model = Item
                fields = ('itemDisplayed',)

class popDisplayedForm(forms.ModelForm):
            class Meta:
                model = Pop
                fields = ('popDisplayed',)
        