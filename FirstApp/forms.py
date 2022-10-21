from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = CommentModel
        exclude = ["post"]
        error_messages = {"username": {"required": "The username is required!"},
                          "comment": {"required": "Enter a comment!"}}