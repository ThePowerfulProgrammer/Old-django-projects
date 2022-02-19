from django import forms 
from django.contrib.auth import get_user_model

# Inherited User model
User = get_user_model()

# Create user
class registerForm(forms.Form):
    # User requires username,email and password
    username = forms.CharField(label='Name', max_length=100)
    username.widget.attrs.update({'class': 'form-control', 'placeholder': 'username'})

    email = forms.EmailField()
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'email'})

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    def clean(self):
        cleaned_data = super().clean()
        validpassword = cleaned_data['password1']
        validpassword2 = cleaned_data['password2']
        if validpassword != validpassword2:
            raise forms.ValidationError('Passwords must match! ')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)

        if qs.exists():
            raise forms.ValidationError('Username is invalid!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)

        if qs.exists():
            raise forms.ValidationError('Email is invalid')
        return email


# Login user
class loginForm(forms.Form):
    username = forms.CharField(label='Name', max_length=100)
    username.widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)

        if not qs.exists():
            raise forms.ValidationError('This is an invalid user')
        return username

