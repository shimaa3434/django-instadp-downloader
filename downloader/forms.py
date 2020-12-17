from django import forms


class UserInput(forms.Form):
    username_ip = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': "form-control form__item", 'placeholder': 'Username'}))
