from django import forms
from commentary.models import Commentary

class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("comment", "post")