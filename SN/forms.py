from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from SN.models import User, Post


# from djangoApplication.models import *
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    avatar = forms.ImageField(required=False, label='Avatar')
    class Meta:
        model =  User
        fields = ('username', 'email', 'avatar', 'bio','password1', 'password2')


class LikeForm(forms.Form):
    post_id = forms.IntegerField(widget=forms.HiddenInput())



class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class addPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image','description')

class AvatarUploadForm(forms.Form):
    avatar = forms.ImageField()