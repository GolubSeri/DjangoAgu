from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Comment


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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']

    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        """Make sure people don't use my name"""
        data = self.cleaned_data['name']
        if not self.request.user.is_authenticated and data.lower().strip() == 'samuel':
            raise ValidationError("Sorry, you cannot use this name.")
        return data
