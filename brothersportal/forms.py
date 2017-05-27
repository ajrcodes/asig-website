from django import forms
from datetime import date


class SearchBrothersForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    year = forms.ChoiceField(choices=(('', "-----"),
                                      ("1st", "1st"),
                                      ("2nd", "2nd"),
                                      ("3rd", "3rd"),
                                      ("4th", "4th"),
                                      ("5th", "5th"),
                                      ("Alumni", "Alumni")),
                             required=False)
    grad_year = forms.IntegerField(date.today().year + 6, 2012, required=False)
    pledge_class = forms.CharField(required=False)
    major = forms.CharField(required=False)
    company = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
