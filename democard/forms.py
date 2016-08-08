import re
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm

class IDForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(IDForm, self).__init__(*args, **kwargs)
        sex_choices = (
            ('M', 'Male'),
            ('F', 'Female'),
        )
        self.fields['first_name'] = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Fist Name"))
        self.fields['last_name'] = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Last Name"))
        self.fields['id'] = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=200)), label=_("Profile Image"))
        self.fields['age'] = forms.CharField(max_length=3, label=_("Age"))
        self.fields['sex'] = forms.ChoiceField(choices = sex_choices, label=_("Sex"))
