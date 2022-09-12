from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    github_link = forms.CharField()
    # website_link = forms.URLField()
    # instagram_link = forms.URLField(null=True, blank=True)
    # twitter_link = forms.URLField(null=True, blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'github_link']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})


