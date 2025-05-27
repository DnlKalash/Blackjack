from django import forms
from .models import User 
from django.contrib.auth.hashers import make_password
 


class UserForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        from .models import User
        if User.objects(username=username).first():
            raise forms.ValidationError("User with this username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        from .models import User
        if User.objects(email=email).first():
            raise forms.ValidationError("User with this email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

    def save(self):
        
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['password'])
        )
        user.save()
        return user



