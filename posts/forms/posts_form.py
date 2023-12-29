from django import forms
from posts.models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields=("title", "description")
        # exclude = ["user"]