from django import forms

class EmailContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length=100)
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    #to = forms.EmailField()
    message = forms.CharField(required=True,
                             widget=forms.Textarea)
