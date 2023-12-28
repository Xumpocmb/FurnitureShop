from django import forms


class UserLoginForm(forms.Form):
    class Meta:
        fields = ['username', 'password']

