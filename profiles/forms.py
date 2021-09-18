from django import forms
from .models import Profile,Comment

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'name',
            'bio',
            'image',
        )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
