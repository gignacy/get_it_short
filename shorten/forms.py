from django import forms
from shorten.models import Links

class LinkForm(forms.ModelForm):
    link = forms.CharField(max_length=200)

    class Meta:
        model = Links
        fields = ('link',)