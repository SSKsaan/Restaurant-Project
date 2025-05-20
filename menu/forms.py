from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Write your review here...'
        })
    )
    rating = forms.IntegerField(required=True, min_value=1, max_value=5)
    class Meta:
        model = Review
        fields = {'rating', 'content', 'image'}