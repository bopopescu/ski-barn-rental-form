from django import forms
from .models import User, UserInfo
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user','address', 'city', 'state', 'zipCode','location', 'phone']

class signupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:    
        model = User
        fields = ['email','password']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def save(self, commit = True):
        user = super(signupForm,self).save(commit=False)
        if commit:
            user.save()
        return user

class loginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username = email, password = password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(loginForm, self).clean(*args,**kwargs)

class resetForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
