from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'example@mail.com'}), error_messages={'required':'Enter your email'})
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}), error_messages={'required':'Enter unique username here'})
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}), error_messages={'required':'Enter password'})
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2','first_name','last_name')
                
                
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'example@mail.com'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name')

class ProfileUpdateForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(format ='%Y-%m-%d',attrs={'class':'form-control','type':'date'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Profile
        fields = ('bio','address','profile_picture','dob')
    

class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}),label='Image')
    posttitle = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Title',required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),label='Caption',max_length=200)
    class Meta:
        model = Post
        fields = ('posttitle','description','image')
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Comment
        fields = ('comment',)