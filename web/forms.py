from django import forms
from django.contrib.auth.models import User
from .models import Profile, Blog

class Profileupdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone', 'dob', 'image']

class Blogpost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'desc', 'img']

