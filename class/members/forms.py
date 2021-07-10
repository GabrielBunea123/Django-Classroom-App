from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from classroom.models import Profile
from django.forms import ImageField

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','facebook_url','github_url','instagram_url','profile_pic']

        widgets={
            'bio': forms.Textarea(attrs={'class':'form_control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form_control'}),
            'github_url':forms.TextInput(attrs={'class':'form_control'}),
            'instagram_url':forms.TextInput(attrs={'class':'form_control'})
        }


class EditConfidentialForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    # is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_staff= forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','last_login','date_joined']

class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','github_url','instagram_url','facebook_url','profile_pic']

        widgets = {
            'bio': forms.TextInput(attrs={'class':'form-control'}),
            'github_url': forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            # 'profile_pic' : forms.ImageField(attrs={'class':'form-control'})
        }

