from django import forms
from .models import Comment

class EmailContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length=100)
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    #to = forms.EmailField()
    message = forms.CharField(required=True,
                             widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
