from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age', 'gender']
    password = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Passwords do not match!')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=100, widget=forms.PasswordInput)
