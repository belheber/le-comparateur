from django import forms

class SerachForm(forms.Form):
  search = forms.CharField(label='Product', max_length=100)