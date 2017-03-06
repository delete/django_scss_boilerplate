from django import forms


class CrediCardNumberForm(forms.Form):

    _file = forms.FileField(label='Upload a text file.')
