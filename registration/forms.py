#coding=utf-8
from django import forms
from .models import *
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    address = forms.CharField()
    sex = forms.CharField()
    telephone = forms.CharField()
    
    def clean_password2(self):
        pwd = self.cleaned_data['password']
        pwd2 = self.cleaned_data['password2']

        if pwd == pwd2:
            return pwd

        raise forms.ValidationError('Las claves no coinciden')
    
    def process(self):
        user = User(email=self.cleaned_data['email'])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.set_password(self.cleaned_data['password'])

        user.is_active = False
        user.save()

        prof = UserProfile(user=user)
        prof.address =self.cleaned_data['address']  
        prof.sex = self.cleaned_data['sex']
        prof.telephone = self.cleaned_data['telephone']

        prof.save()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        exclude = ('user', 'movie')
