from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=30,help_text="Maximum 30 characters.")
    last_name = forms.CharField(max_length=150,help_text="Maximum 30 characters.")

    # Override constructor to add class to HTML element (from Bootstrap)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1', 'password2']