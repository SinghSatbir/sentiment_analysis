from django import forms
from twitter_analysis.models import Word


class Form(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
        labels = {'keyword_entered': ''}