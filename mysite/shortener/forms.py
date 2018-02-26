from django import forms

class ShortForm(forms.Form):
	long_link = forms.CharField()