from django import forms


class UserForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "myfield",
        }),
        label="Ваше имя: ",
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "class": "myfield",
        }),
        label="Ваш возраст: ",
    )
