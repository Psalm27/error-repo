from django import forms
from .models import Docs


class DocsForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = ('cv', 'cover_letter', 'intro_letter')

    def __init__(self, *args, **kwargs):
        super(DocsForm, self).__init__(*args, **kwargs)
        self.fields['cv'].widget.attrs.update({'class': 'form-control'})
        self.fields['cover_letter'].widget.attrs.update({'class': 'form-control'})
        self.fields['intro_letter'].widget.attrs.update({'class': 'form-control'})
