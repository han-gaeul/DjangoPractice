from django import forms
from .models import Comment, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie_name', 'grade', 'image', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 필드 목록에서 제외
        exclude = ('review', 'user', )