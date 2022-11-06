from django import forms
from .models import Information

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('info_title', 'info_content', 'image', )