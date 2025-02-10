from .models import Comment, STAR_RATINGS
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=STAR_RATINGS),
        }
