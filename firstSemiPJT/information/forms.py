from django import forms
from .models import Information, Comment

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('info_title', 'info_content', 'image', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'user', )